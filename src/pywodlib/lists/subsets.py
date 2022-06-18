from __future__ import annotations
from collections.abc import Iterator, Sequence
from itertools import compress
from typing import TypeVar

T = TypeVar("T")


def subsets(
    xs: Sequence[T], nonempty: bool = False, proper: bool = False
) -> Iterator[tuple[T, ...]]:
    """
    Returns an iterator over all subsets of the iterable ``xs`` as tuples.  If
    ``nonempty`` is true, only nonempty subsets are returned.  If ``proper`` is
    true, only proper subsets are returned.
    """
    xs = tuple(xs)
    selectors = [False] * len(xs)
    while True:
        if not ((nonempty and not any(selectors)) or (proper and all(selectors))):
            yield tuple(compress(xs, selectors))
        for i in range(len(selectors)):
            selectors[i] = not selectors[i]
            if selectors[i]:
                break
        else:
            break
