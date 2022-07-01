from __future__ import annotations
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar

T = TypeVar("T")


def split_after(
    predicate: Callable[[T], Any], iterable: Iterable[T]
) -> Iterator[list[T]]:
    # cf. split_after from more-itertools
    """
    Return a generator of subsequences of ``iterable``, split after each
    element ``x`` for which ``predicate(x)`` is true.

    If the predicate is true for the last element of ``iterable``, no trailing
    empty list is emitted.

    If ``iterable`` is empty, a generator of one empty list is returned.
    """
    empty = True
    chunk: list[T] = []
    for obj in iterable:
        empty = False
        chunk.append(obj)
        if predicate(obj):
            yield chunk
            chunk = []
    if empty or chunk:
        yield chunk
