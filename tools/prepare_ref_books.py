#!/usr/bin/env python3
"""Download and convert the C books selected from PV-Books.

PV-Books stores most PDFs with Git LFS.  A plain ``git clone`` leaves small
pointer files behind, so this script resolves the pointer files through
GitHub's media endpoint, copies the selected books into ``.ref/books``, and
converts them to Markdown in ``.ref/markdown``.

The list intentionally excludes the C++ directory and C++-titled books.  It
includes core C books, C algorithm/data-structure books, and C/POSIX systems
books that are useful for understanding C in real programs.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / ".ref"
PV = REF / "PV-Books"
BOOKS_DIR = REF / "books"
MARKDOWN_DIR = REF / "markdown"
OCR_DIR = REF / "ocr"
MANIFEST = REF / "books-manifest.json"

REPO = "PaleVerge/PV-Books"
BRANCH = "main"
MEDIA_BASE = f"https://media.githubusercontent.com/media/{REPO}/{BRANCH}/"
LFS_POINTER_PREFIX = "version https://git-lfs.github.com/spec/v1"


@dataclass(frozen=True)
class Book:
    source: str
    title: str
    group: str
    note: str = ""


# Curated C-focused selection.  C++/ is excluded; C++-titled files elsewhere
# are excluded too.  C-adjacent systems books are marked in ``group``.
BOOKS = [
    Book("C/C程序设计语言（第2版）.pdf", "C程序设计语言（第2版）", "C core", "K&R"),
    Book(
        "C/C Primer Plus 第6版 中文版（史蒂芬·普拉达）.pdf",
        "C Primer Plus 第6版 中文版",
        "C core",
    ),
    Book("C/C Primer Plus.epub", "C Primer Plus", "C core", "EPUB edition"),
    Book("C/C陷阱与缺陷.pdf", "C陷阱与缺陷", "C core"),
    Book("C/C语言接口与实现.pdf", "C语言接口与实现", "C core"),
    Book("Algorithms/C专家编程.pdf", "C专家编程", "C core"),
    Book("Algorithms/狂人C程序员入门必备.pdf", "狂人C程序员入门必备", "C core"),
    Book(
        "Algorithms/C语言深度解剖(完美高清文字版).pdf",
        "C语言深度解剖",
        "C core",
    ),
    Book(
        "Algorithms/数据结构与算法分析：C语言描述（第2版）.pdf",
        "数据结构与算法分析：C语言描述（第2版）",
        "C algorithms",
    ),
    Book("Algorithms/C语言程序190例.doc", "C语言程序190例", "C algorithms"),
    Book(
        "Algorithms/C语言趣味程序设计编程百例精解.doc",
        "C语言趣味程序设计编程百例精解",
        "C algorithms",
    ),
    Book("Algorithms/C语言算法100例.doc", "C语言算法100例", "C algorithms"),
    Book(
        "Linux/UNIX环境高级编程(第三版).pdf",
        "UNIX环境高级编程(第三版)",
        "C systems / POSIX",
        "APUE",
    ),
    Book(
        "Linux/UNIX网络编程卷1：套接字API.pdf",
        "UNIX网络编程卷1：套接字API",
        "C systems / POSIX",
        "UNP volume 1",
    ),
    Book(
        "Linux/UNIX网络编程卷2：进程间通信.pdf",
        "UNIX网络编程卷2：进程间通信",
        "C systems / POSIX",
        "UNP volume 2",
    ),
    Book("Linux/UNIX编程艺术.pdf", "UNIX编程艺术", "C systems / POSIX"),
    Book("Linux/跟我一起写makefile.pdf", "跟我一起写Makefile", "C tooling"),
    Book(
        "Computer-system/深入理解计算机系统（第3版）.pdf",
        "深入理解计算机系统（第3版）",
        "C systems / POSIX",
        "CSAPP",
    ),
    Book(
        "Others/程序员的自我修养：链接、装载与库.pdf",
        "程序员的自我修养：链接、装载与库",
        "C systems / POSIX",
        "linking and loading",
    ),
    Book(
        "Clean-code/程序设计实践.pdf",
        "程序设计实践",
        "C craft",
        "language-agnostic but C-centric examples",
    ),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def lfs_pointer(path: Path) -> tuple[str, int] | None:
    try:
        first = path.read_text(encoding="utf-8", errors="replace")[:200]
    except OSError:
        return None
    if not first.startswith(LFS_POINTER_PREFIX):
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    oid = ""
    size = 0
    for line in text.splitlines():
        if line.startswith("oid sha256:"):
            oid = line.split(":", 1)[1].strip()
        elif line.startswith("size "):
            size = int(line.split()[1])
    return oid, size


def media_url(source: str) -> str:
    return MEDIA_BASE + urllib.parse.quote(source)


def download_file(url: str, destination: Path, expected_size: int | None = None) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".part")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "clings-ref-book-prep/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        with temporary.open("wb") as handle:
            shutil.copyfileobj(response, handle, length=1024 * 1024)
    if expected_size is not None and temporary.stat().st_size != expected_size:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(
            f"size mismatch for {url}: expected {expected_size}, "
            f"got {temporary.stat().st_size if temporary.exists() else 'missing'}"
        )
    temporary.replace(destination)


def copy_or_download(book: Book, force: bool = False) -> dict[str, object]:
    source = PV / book.source
    destination = BOOKS_DIR / book.source
    if not source.exists():
        return {"source": book.source, "status": "missing-source"}

    pointer = lfs_pointer(source)
    if destination.exists() and not force:
        if pointer is None or not lfs_pointer(destination):
            return {
                "source": book.source,
                "destination": str(destination.relative_to(ROOT)),
                "status": "already-present",
                "size": destination.stat().st_size,
            }

    if pointer is None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        status = "copied"
    else:
        expected_size = pointer[1]
        download_file(media_url(book.source), destination, expected_size)
        status = "downloaded-lfs"

    return {
        "source": book.source,
        "destination": str(destination.relative_to(ROOT)),
        "status": status,
        "size": destination.stat().st_size,
    }


class HtmlToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0
        self.heading_level = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        tag = tag.lower()
        if tag in {"script", "style"}:
            self.skip_depth += 1
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_level = int(tag[1])
            self.parts.append("\n\n" + "#" * self.heading_level + " ")
        elif tag in {"p", "div", "section", "article", "blockquote"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "pre":
            self.parts.append("\n\n```\n")
        elif tag == "code" and self.heading_level == 0:
            self.parts.append("`")
        elif tag == "tr":
            self.parts.append("\n")
        elif tag in {"td", "th"}:
            self.parts.append(" | ")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n")
            self.heading_level = 0
        elif tag in {"p", "div", "section", "article", "blockquote", "li"}:
            self.parts.append("\n")
        elif tag == "pre":
            self.parts.append("\n```\n")
        elif tag == "code" and self.heading_level == 0:
            self.parts.append("`")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def markdown(self) -> str:
        text = html.unescape("".join(self.parts))
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def epub_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        opf_name = ""
        container_name = "META-INF/container.xml"
        if container_name in names:
            container = ET.fromstring(archive.read(container_name))
            for element in container.iter():
                if element.tag.endswith("rootfile"):
                    opf_name = element.attrib.get("full-path", "")
                    break

        spine_files: list[str] = []
        title = path.stem
        if opf_name and opf_name in names:
            opf = ET.fromstring(archive.read(opf_name))
            manifest: dict[str, str] = {}
            for element in opf.iter():
                if element.tag.endswith("item"):
                    manifest[element.attrib.get("id", "")] = element.attrib.get(
                        "href", ""
                    )
                elif element.tag.endswith("itemref"):
                    item = manifest.get(element.attrib.get("idref", ""))
                    if item:
                        spine_files.append(item)
                elif element.tag.endswith("title") and element.text:
                    title = element.text.strip()
            base = Path(opf_name).parent
            spine_files = [str((base / item).as_posix()) for item in spine_files]

        if not spine_files:
            spine_files = sorted(
                name
                for name in names
                if name.lower().endswith((".html", ".xhtml", ".htm"))
            )

        pieces: list[str] = []
        for name in spine_files:
            if name not in names:
                continue
            parser = HtmlToMarkdown()
            parser.feed(archive.read(name).decode("utf-8", errors="replace"))
            text = parser.markdown()
            if text:
                pieces.extend([f"<!-- {name} -->", "", text, ""])
        return "\n".join(pieces).strip() + "\n"


def pdf_text(path: Path) -> str:
    with tempfile.TemporaryDirectory(prefix="clings-ref-pdf-") as directory:
        output = Path(directory) / "book.txt"
        result = subprocess.run(
            ["pdftotext", "-layout", str(path), str(output)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or "pdftotext failed")
        text = output.read_text(encoding="utf-8", errors="replace")
    text = text.replace("\f", "\n\n---\n\n")
    text = text.replace("\x00", "")
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def pdf_pages(path: Path) -> int:
    try:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            check=False,
        )
    except OSError:
        return 0
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return 0
    return 0


def ocr_text(source: str) -> str | None:
    """Return OCR text for a source PDF if it has been generated."""
    path = OCR_DIR / Path(source).with_suffix(".txt")
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")

    def page_heading(match: re.Match[str]) -> str:
        return f"\n\n---\n\n## Page {int(match.group(1))}\n\n"

    text = re.sub(r"<!--\s*page-(\d+)\s*-->", page_heading, text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def doc_text(path: Path) -> str:
    home = Path(tempfile.mkdtemp(prefix="clings-ref-soffice-"))
    output_dir = home / "out"
    output_dir.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["HOME"] = str(home)
    subprocess.run(
        [
            "soffice",
            "--headless",
            f"-env:UserInstallation=file://{home / 'profile'}",
            "--convert-to",
            "txt:Text (encoded):UTF8",
            "--outdir",
            str(output_dir),
            str(path),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=environment,
        timeout=300,
    )
    candidates = list(output_dir.glob("*.txt"))
    if not candidates:
        raise RuntimeError(f"soffice produced no text for {path}")
    text = candidates[0].read_text(encoding="utf-8", errors="replace")
    shutil.rmtree(home, ignore_errors=True)
    return text.strip() + "\n"


def convert_book(book: Book) -> dict[str, object]:
    source = BOOKS_DIR / book.source
    markdown = MARKDOWN_DIR / Path(book.source).with_suffix(".md")
    if not source.exists():
        return {"source": book.source, "conversion": "missing-source"}

    markdown.parent.mkdir(parents=True, exist_ok=True)
    suffix = source.suffix.lower()
    try:
        pages = 0
        if suffix == ".pdf":
            pages = pdf_pages(source)
            override = ocr_text(book.source)
            if override is not None:
                text = override
                quality = "ocr"
            else:
                text = pdf_text(source)
                quality = "ok"
        elif suffix == ".epub":
            text = epub_text(source)
            quality = "ok"
        elif suffix in {".doc", ".docx"}:
            text = doc_text(source)
            quality = "ok"
        elif suffix in {".txt", ".md"}:
            text = source.read_text(encoding="utf-8", errors="replace")
            quality = "ok"
        else:
            return {"source": book.source, "conversion": f"unsupported {suffix}"}

        if suffix == ".pdf" and quality != "ocr":
            characters_per_page = len(text) / pages if pages else len(text)
            if len(text) < 2000 or characters_per_page < 100:
                quality = "ocr-required"

        body = [
            f"# {book.title}",
            "",
            f"> Source: `{book.source}`",
            f"> Group: {book.group}",
            f"> Converted by `tools/prepare_ref_books.py`.",
            "",
        ]
        if quality == "ocr-required":
            body.extend(
                [
                    "> **OCR required:** this PDF appears to be image-only or has",
                    f"> almost no text layer ({len(text)} characters across {pages}",
                    "> pages). The Markdown below is therefore incomplete. Run an OCR",
                    "> tool such as `ocrmypdf`/Tesseract, then rerun the converter.",
                    "",
                ]
            )
        elif quality == "ocr":
            body.extend(
                [
                    "> **OCR text:** generated with Tesseract `chi_sim+eng`.",
                    "> OCR may misrecognize characters or code; check the PDF for",
                    "> exact code snippets.",
                    "",
                ]
            )
        markdown.write_text("\n".join(body) + text, encoding="utf-8")
        return {
            "source": book.source,
            "markdown": str(markdown.relative_to(ROOT)),
            "conversion": "ok",
            "quality": quality,
            "pages": pages,
            "characters": len(text),
        }
    except Exception as error:  # noqa: BLE001 - report per-book failures
        if markdown.exists() and markdown.stat().st_size > 1000:
            return {
                "source": book.source,
                "markdown": str(markdown.relative_to(ROOT)),
                "conversion": "ok",
                "quality": "cached",
                "error": f"{type(error).__name__}: {error}",
            }
        return {
            "source": book.source,
            "conversion": "failed",
            "error": f"{type(error).__name__}: {error}",
        }


def move_reference_repo(source: Path, destination: Path) -> str:
    if destination.exists():
        return f"{destination.name}: already present"
    if not source.exists():
        return f"{destination.name}: source {source} not found"
    shutil.move(str(source), str(destination))
    return f"{destination.name}: moved from {source}"


def write_index(records: list[dict[str, object]]) -> None:
    lines = [
        "# .ref",
        "",
        "This directory contains the local reference material used to design and",
        "review the clings curriculum.",
        "",
        "- `PV-Books/`: full clone of https://github.com/PaleVerge/PV-Books.",
        "- `books/`: C-focused books selected from PV-Books.",
        "- `markdown/`: Markdown conversions of the selected books.",
        "- `ocr/`: OCR text for scanned books that have been processed.",
        "- `cpplings/`, `cplings/`: the two reference exercise repositories.",
        "- `books-manifest.json`: machine-readable download/conversion manifest.",
        "- `OCR-REQUIRED.md`: scanned PDFs that need OCR for full-text Markdown.",
        "- `../docs/gap-analysis.md`: what the books show is still missing from",
        "  the exercise curriculum.",
        "",
        "C++ books and the `C++/` directory are intentionally excluded.",
        "",
        "## Selected C books",
        "",
        "| Group | Title | Source | Markdown | Quality |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| {group} | {title} | `{source}` | `{markdown}` | {quality} |".format(
                group=record.get("group", ""),
                title=record.get("title", ""),
                source=record.get("source", ""),
                markdown=record.get("markdown", ""),
                quality=record.get("quality", record.get("conversion", "")),
            )
        )
    lines.append("")
    (REF / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_ocr_list(records: list[dict[str, object]]) -> None:
    lines = [
        "# OCR required",
        "",
        "The following PDFs are image-only or have an almost empty text layer.",
        "Their Markdown files contain only the extracted fragments; run OCR if",
        "you need full-text search for them.",
        "",
        "| Title | Pages | Extracted characters | PDF | Markdown |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    found = False
    for record in records:
        if record.get("quality") != "ocr-required":
            continue
        found = True
        lines.append(
            "| {title} | {pages} | {characters} | `{source}` | `{markdown}` |".format(
                title=record.get("title", ""),
                pages=record.get("pages", 0),
                characters=record.get("characters", 0),
                source=record.get("source", ""),
                markdown=record.get("markdown", ""),
            )
        )
    if not found:
        lines.append("| (none) | 0 | 0 | - | - |")
    lines.extend(
        [
            "",
            "Suggested command after installing Tesseract/ocrmypdf:",
            "",
            "```sh",
            "ocrmypdf --skip-text -l chi_sim+eng input.pdf output.pdf",
            "python3 tools/prepare_ref_books.py --skip-download",
            "```",
            "",
        ]
    )
    (REF / "OCR-REQUIRED.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=4, help="parallel downloads")
    parser.add_argument("--force", action="store_true", help="re-download and re-convert")
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="only convert files already present in .ref/books",
    )
    args = parser.parse_args()

    REF.mkdir(exist_ok=True)
    BOOKS_DIR.mkdir(exist_ok=True)
    MARKDOWN_DIR.mkdir(exist_ok=True)

    records: list[dict[str, object]] = []
    if not args.skip_download:
        print(f"downloading/copying {len(BOOKS)} selected books ...")
        lock = threading.Lock()
        completed = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {
                pool.submit(copy_or_download, book, args.force): book
                for book in BOOKS
            }
            for future in concurrent.futures.as_completed(futures):
                book = futures[future]
                try:
                    result = future.result()
                except Exception as error:  # noqa: BLE001 - report per-book failures
                    result = {
                        "source": book.source,
                        "status": "failed",
                        "error": f"{type(error).__name__}: {error}",
                    }
                with lock:
                    completed += 1
                    size = result.get("size")
                    size_text = f"{size / 1024 / 1024:.1f} MiB" if size else "-"
                    print(
                        f"[{completed:02d}/{len(BOOKS)}] "
                        f"{result.get('status', 'unknown'):16} {size_text:>10} "
                        f"{book.source}"
                    )
                records.append({**result, "title": book.title, "group": book.group})

    print(f"converting {len(BOOKS)} books to Markdown ...")
    conversions = []
    for book in BOOKS:
        result = convert_book(book)
        conversions.append({**result, "title": book.title, "group": book.group})
        print(
            f"{result.get('conversion', 'unknown'):12} "
            f"{result.get('characters', ''):>10} {book.source}"
        )

    by_source = {record.get("source"): record for record in records}
    merged: list[dict[str, object]] = []
    for conversion in conversions:
        base = by_source.get(conversion.get("source"), {})
        merged.append({**base, **conversion})

    MANIFEST.write_text(
        json.dumps({"books": merged}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_index(merged)
    write_ocr_list(merged)

    print(move_reference_repo(Path("/tmp/ref-cpplings"), REF / "cpplings"))
    print(move_reference_repo(Path("/tmp/ref-cplings"), REF / "cplings"))
    print(f"wrote {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
