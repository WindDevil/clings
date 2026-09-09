"""Shared data structures for the clings exercise generator."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ExerciseSpec:
    topic: str
    slug: str
    title: str
    objective: str
    reference: str
    hint: str
    code: str
    tests: str
    breaks: list[tuple[str, str]] = field(default_factory=list)
    compile_fail: bool = False
    files: dict[str, str] | None = None
    file_breaks: list[tuple[str, str, str]] = field(default_factory=list)

    @property
    def ident(self) -> str:
        return f"{self.topic}/{self.slug}"


def ex(
    topic: str,
    slug: str,
    title: str,
    objective: str,
    reference: str,
    hint: str,
    code: str,
    tests: str,
    breaks: list[tuple[str, str]],
    compile_fail: bool = False,
) -> ExerciseSpec:
    return ExerciseSpec(
        topic=topic,
        slug=slug,
        title=title,
        objective=objective,
        reference=reference,
        hint=hint,
        code=code.strip("\n") + "\n",
        tests=tests.strip("\n") + "\n",
        breaks=breaks,
        compile_fail=compile_fail,
    )


def project(
    topic: str,
    slug: str,
    title: str,
    objective: str,
    reference: str,
    hint: str,
    files: dict[str, str],
    file_breaks: list[tuple[str, str, str]] | None = None,
) -> ExerciseSpec:
    """Create a multi-file project exercise.

    ``files`` maps relative paths (for example ``main.c`` and ``math_utils.c``)
    to complete file contents.  ``file_breaks`` entries are
    ``(filename, correct_text, learner_text)`` replacements.
    """
    return ExerciseSpec(
        topic=topic,
        slug=slug,
        title=title,
        objective=objective,
        reference=reference,
        hint=hint,
        code="",
        tests="",
        breaks=[],
        files={name: content.strip("\n") + "\n" for name, content in files.items()},
        file_breaks=file_breaks or [],
    )
