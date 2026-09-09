#!/usr/bin/env python3
"""Generate clings exercises, solutions, templates, and documentation.

The generated files are checked into the repository.  Keeping the generator
around makes it easy to add a new exercise consistently:

    python3 tools/generate_exercises.py

Each exercise spec contains the correct code.  The broken learner version is
created by applying the spec's ``breaks`` replacements.  This guarantees that
the exercise and solution stay in sync.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from spec import ExerciseSpec

ROOT = Path(__file__).resolve().parent.parent
EXERCISES_DIR = ROOT / "exercises"
SOLUTIONS_DIR = ROOT / "solutions"
TEMPLATES_DIR = ROOT / "templates"


def header(spec: ExerciseSpec) -> str:
    return f"""/*
 * clings exercise: {spec.ident}
 * title: {spec.title}
 * objective: {spec.objective}
 * reference: {spec.reference}
 * hint: {spec.hint}
 */
"""


def program(spec: ExerciseSpec, code: str) -> str:
    return (
        header(spec)
        + '\n#include "clings/test.h"\n\n'
        + code
        + "\nint main(void)\n{\n"
        + indent(spec.tests, "    ")
        + "    return clings_report();\n}\n"
    )


def indent(text: str, prefix: str) -> str:
    return "".join(prefix + line if line.strip() else line for line in text.splitlines(True))


def broken_code(spec: ExerciseSpec) -> str:
    code = spec.code
    for correct, broken in spec.breaks:
        if correct not in code:
            raise SystemExit(
                f"{spec.ident}: break pattern not found in correct code:\n{correct}"
            )
        code = code.replace(correct, broken, 1)
    return code


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def load_specs() -> list[ExerciseSpec]:
    from specs_00_04 import SPECS as specs_00_04
    from specs_05_08 import SPECS as specs_05_08
    from specs_09_12 import SPECS as specs_09_12

    specs = specs_00_04 + specs_05_08 + specs_09_12
    seen: set[str] = set()
    for spec in specs:
        if spec.ident in seen:
            raise SystemExit(f"duplicate exercise id: {spec.ident}")
        seen.add(spec.ident)
    return specs


TOPIC_TITLES = {
    "00_getting_started": "Getting Started",
    "01_types_variables": "Types, Variables, and Storage",
    "02_operators": "Operators and Expressions",
    "03_control_flow": "Control Flow",
    "04_functions": "Functions and Scope",
    "05_arrays_strings": "Arrays and Strings",
    "06_pointers": "Pointers and Memory Layout",
    "07_dynamic_memory": "Dynamic Memory and Data Structures",
    "08_structs_unions_enums": "Structs, Unions, Enums, and Bitfields",
    "09_preprocessor": "Preprocessor and Macros",
    "10_stdlib_io": "Standard Library and File I/O",
    "11_ub_safety": "Undefined Behavior, Safety, and Portability",
    "12_advanced_c": "Advanced C Features",
}


def topic_readme_contents(specs: list[ExerciseSpec]) -> dict[Path, str]:
    contents: dict[Path, str] = {}
    by_topic: dict[str, list[ExerciseSpec]] = {}
    for spec in specs:
        by_topic.setdefault(spec.topic, []).append(spec)

    for topic, topic_specs in by_topic.items():
        lines = [
            f"# {TOPIC_TITLES.get(topic, topic)}",
            "",
            "Run an exercise with:",
            "",
            "```sh",
            f"./clings run {topic_specs[0].slug}",
            "```",
            "",
            "| Exercise | Objective | Reference |",
            "| --- | --- | --- |",
        ]
        for spec in topic_specs:
            lines.append(
                f"| `{spec.slug}` | {spec.objective} | {spec.reference} |"
            )
        lines.append("")
        contents[EXERCISES_DIR / topic / "README.md"] = "\n".join(lines)
    return contents


def curriculum_content(specs: list[ExerciseSpec]) -> str:
    by_topic: dict[str, list[ExerciseSpec]] = {}
    for spec in specs:
        by_topic.setdefault(spec.topic, []).append(spec)

    lines = [
        "# Curriculum and coverage map",
        "",
        "This map connects each topic to the exercises that teach it and to the",
        "corresponding section of *C语言深度解剖*.  The book is a deep-dive",
        "companion; the exercises also cover standard-library, tooling, and",
        "portability topics that are outside the book's original scope.",
        "",
        f"Total exercises: **{len(specs)}** across **{len(by_topic)}** topics.",
        "",
    ]
    for topic, topic_specs in by_topic.items():
        lines.extend(
            [
                f"## {topic} - {TOPIC_TITLES.get(topic, topic)}",
                "",
                "| Exercise | Objective | Book reference |",
                "| --- | --- | --- |",
            ]
        )
        for spec in topic_specs:
            lines.append(
                f"| `{spec.ident}` | {spec.objective} | {spec.reference} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Cross-cutting knowledge checklist",
            "",
            "The following C knowledge areas are deliberately covered by the",
            "exercises and supporting documentation:",
            "",
            "- Translation units, declarations, definitions, linkage, and the",
            "  preprocessing/compiling/assembling/linking pipeline.",
            "- All standard integer and floating types, `<limits.h>` and",
            "  `<float.h>`, signed/unsigned conversions, overflow, and casts.",
            "- Constants, `const`, `enum`, `#define`, storage classes, scope,",
            "  lifetime, and name lookup.",
            "- Every operator family: arithmetic, relational, logical,",
            "  bitwise, shift, assignment, conditional, comma, `sizeof`,",
            "  address-of, dereference, member access, and casts.",
            "- Sequence points, short-circuit evaluation, precedence,",
            "  associativity, and side effects.",
            "- `if`, `switch`, `for`, `while`, `do-while`, `break`,",
            "  `continue`, `goto`, nested control flow, and state machines.",
            "- Function declarations, definitions, parameters, return values,",
            "  recursion, `static`, `inline`, function pointers, callbacks,",
            "  variadic functions, and scope.",
            "- Arrays, array decay, multidimensional arrays, variable-length",
            "  arrays, string literals, mutable strings, `<string.h>`,",
            "  bounded formatting, tokenization, and UTF-8 basics.",
            "- Pointer representation, `NULL`, pointer arithmetic, arrays vs",
            "  pointers, `const` placement, multi-level pointers, `void *`,",
            "  function pointers, dangling/wild pointers, `restrict`, and",
            "  endianness.",
            "- `malloc`, `calloc`, `realloc`, `free`, ownership, leaks,",
            "  use-after-free, double free, bounds, flexible array members,",
            "  linked lists, dynamic arrays, and basic allocator reasoning.",
            "- Structs, nested structs, padding/alignment, bitfields, unions,",
            "  enums, typedefs, designated initializers, compound literals,",
            "  `offsetof`, and `container_of`.",
            "- Object-like and function-like macros, macro hygiene,",
            "  stringizing, token pasting, conditional compilation, include",
            "  guards, variadic macros, X-macros, and `#pragma`.",
            "- `printf`/`scanf`, `strtol`, `errno`, `qsort`, `bsearch`,",
            "  `math.h`, `time.h`, `rand`, `ctype.h`, environment/exit,",
            "  text and binary file I/O, seeking, and error handling.",
            "- Undefined behavior, implementation-defined behavior, signed",
            "  overflow, uninitialized reads, out-of-bounds access, sequence",
            "  points, strict aliasing, alignment, and null dereference.",
            "- Advanced C11/C17 features: `_Generic`, `_Static_assert`,",
            "  `_Alignof`/`_Alignas`, atomics, POSIX threads, `setjmp`,",
            "  `longjmp`, signals, and variadic functions.",
            "",
            "## Suggested learning path",
            "",
            "1. `00_getting_started` and `01_types_variables`",
            "2. `02_operators` and `03_control_flow`",
            "3. `04_functions` and `05_arrays_strings`",
            "4. `06_pointers` and `07_dynamic_memory`",
            "5. `08_structs_unions_enums` and `09_preprocessor`",
            "6. `10_stdlib_io` and `11_ub_safety`",
            "7. `12_advanced_c`",
            "",
            "Do not read the solutions until you have run the exercise and",
            "looked at the compiler or test output.  The point is to learn the",
            "feedback loop, not to collect green checkmarks.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that generated files are up to date without writing",
    )
    args = parser.parse_args()

    specs = load_specs()
    generated: dict[Path, str] = {}
    for spec in specs:
        correct = program(spec, spec.code)
        learner = program(spec, broken_code(spec))
        generated[EXERCISES_DIR / spec.topic / f"{spec.slug}.c"] = learner
        generated[TEMPLATES_DIR / spec.topic / f"{spec.slug}.c"] = learner
        generated[SOLUTIONS_DIR / spec.topic / f"{spec.slug}.c"] = correct

    generated.update(topic_readme_contents(specs))
    generated[ROOT / "docs" / "curriculum.md"] = curriculum_content(specs)

    stale = [
        path
        for path, content in generated.items()
        if not path.exists() or path.read_text(encoding="utf-8") != content
    ]
    if args.check:
        if stale:
            for path in stale:
                print(f"stale: {path.relative_to(ROOT)}")
            return 1
        print(f"{len(generated)} generated files are up to date")
        return 0

    for path, content in generated.items():
        write(path, content)
    print(
        f"generated {len(specs)} exercises, {len(specs)} solutions, "
        f"and {len(specs)} templates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
