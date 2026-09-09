#!/usr/bin/env python3
"""Convert the supplied C language book PDF into a readable Markdown file.

The conversion is intentionally conservative.  PDF text extraction cannot
recover every table or code block perfectly, but the result is searchable and
keeps the chapter/section structure.  The original PDF remains the source of
truth for typography and figures.

Usage:

    python3 tools/pdf_to_markdown.py
    python3 tools/pdf_to_markdown.py --input book.pdf --output docs/reference/book.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "C语言深度解剖(完美高清文字版).pdf"
DEFAULT_OUTPUT = ROOT / "docs" / "reference" / "c-language-deep-dissection.md"

CHAPTER_RE = re.compile(r"^第[一二三四五六七八九十百零〇0-9]+章\s*(.*)$")
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)*)[，,]\s*(.+)$")
TOC_RE = re.compile(r"^(.*?)\.{3,}\s*(\d+)\s*$")


def extract_text(pdf: Path) -> str:
    with tempfile.TemporaryDirectory(prefix="clings-pdf-") as directory:
        text_path = Path(directory) / "book.txt"
        subprocess.run(
            ["pdftotext", "-layout", str(pdf), str(text_path)],
            check=True,
        )
        return text_path.read_text(encoding="utf-8", errors="replace")


def is_cjk(character: str) -> bool:
    return bool(character) and (
        "\u4e00" <= character <= "\u9fff"
        or "\u3400" <= character <= "\u4dbf"
        or character in "，。、；：？！“”‘’（）《》【】—…"
    )


def join_lines(lines: list[str]) -> str:
    result = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not result:
            result = line
            continue
        if is_cjk(result[-1]) or is_cjk(line[0]):
            result += line
        else:
            result += " " + line
    return result


def normalize_heading(title: str) -> str:
    title = re.sub(r"\.{3,}\s*\d+\s*$", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def looks_like_code(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if line.startswith("    ") or line.startswith("\t"):
        # Indentation alone is common in the PDF's prose.  Only treat it as
        # code when it also contains C-like punctuation and no CJK text.
        if re.search(r"[\u4e00-\u9fff]", stripped):
            return False
        return bool(re.search(r"[{}();=]|->|##|\+\+|--", stripped))
    code_markers = (
        "#include",
        "#define",
        "#if",
        "#endif",
        "printf(",
        "scanf(",
        "return ",
        "int ",
        "char ",
        "struct ",
        "void ",
        "for (",
        "while (",
        "if (",
        "switch (",
        "sizeof(",
    )
    if stripped.startswith(code_markers):
        return True
    return stripped in {"{", "}"} or stripped.endswith(";")


def convert(text: str, source_name: str) -> str:
    output: list[str] = [
        "# C 语言深度解剖（PDF 转 Markdown）",
        "",
        f"> 源文件：`{source_name}`",
        ">",
        "> 本文件由 `tools/pdf_to_markdown.py` 自动转换，用于检索和课程映射。",
        "> 排版、图表和代码片段可能因 PDF 文本抽取而失真；遇到细节请回看原 PDF。",
        "",
    ]

    paragraph: list[str] = []
    code_block: list[str] = []
    in_toc = False

    def flush_paragraph() -> None:
        if paragraph:
            output.append(join_lines(paragraph))
            output.append("")
            paragraph.clear()

    def flush_code() -> None:
        if code_block:
            output.append("```c")
            output.extend(code_block)
            output.append("```")
            output.append("")
            code_block.clear()

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            flush_code()
            continue

        if re.fullmatch(r"\d+", stripped):
            continue

        toc_match = TOC_RE.match(stripped)
        if toc_match:
            flush_paragraph()
            flush_code()
            title = normalize_heading(toc_match.group(1))
            if title:
                if not in_toc:
                    output.extend(["## 目录", ""])
                    in_toc = True
                output.append(f"- {title}")
            continue

        chapter_match = CHAPTER_RE.match(stripped)
        if chapter_match:
            flush_paragraph()
            flush_code()
            in_toc = False
            output.extend([f"# {normalize_heading(stripped)}", ""])
            continue

        section_match = SECTION_RE.match(stripped)
        if section_match:
            flush_paragraph()
            flush_code()
            number, title = section_match.groups()
            depth = number.count(".") + 2
            output.extend([f"{'#' * min(depth, 6)} {number} {title}", ""])
            continue

        if looks_like_code(line):
            flush_paragraph()
            code_block.append(line.rstrip())
            continue

        if code_block:
            flush_code()
        paragraph.append(line)

    flush_paragraph()
    flush_code()

    # Collapse more than one blank line and remove trailing whitespace.
    cleaned: list[str] = []
    blank = False
    for line in output:
        if line.strip():
            cleaned.append(line.rstrip())
            blank = False
        elif not blank:
            cleaned.append("")
            blank = True
    return "\n".join(cleaned).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"input PDF not found: {args.input}")

    text = extract_text(args.input)
    markdown = convert(text, args.input.name)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown, encoding="utf-8")
    print(f"wrote {args.output} ({len(markdown.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
