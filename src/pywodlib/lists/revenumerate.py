from __future__ import annotations
from collections.abc import Iterator, Sequence
from typing import TypeVar

T = TypeVar("T")


def revenumerate(
    sequence: Sequence[T], start: int | None = None
) -> Iterator[tuple[int, T]]:
    """Like ``enumerate()``, but yields pairs in reverse order"""
    i = len(sequence) - 1 if start is None else start
    rev = reversed(sequence)
    while True:
        try:
            x = next(rev)
        except StopIteration:
            break
        else:
            yield (i, x)
            i -= 1
