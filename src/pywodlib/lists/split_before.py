from __future__ import annotations
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar

T = TypeVar("T")


def split_before(
    predicate: Callable[[T], Any], iterable: Iterable[T]
) -> Iterator[list[T]]:
    # cf. split_before from more-itertools
    """
    Return a generator of subsequences of ``iterable``, split before each
    element ``x`` for which ``predicate(x)`` is true.

    If the predicate is true for the first element of ``iterable``, no leading
    empty list is emitted.

    If ``iterable`` is empty, a generator of one empty list is returned.
    """
    chunk: list[T] = []
    for obj in iterable:
        if predicate(obj):
            if chunk:
                yield chunk
            chunk = [obj]
        else:
            chunk.append(obj)
    yield chunk
