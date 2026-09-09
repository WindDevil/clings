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
