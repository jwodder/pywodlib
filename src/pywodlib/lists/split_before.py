from __future__ import annotations
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar

T = TypeVar("T")


def split_before(
    predicate: Callable[[T], Any], iterable: Iterable[T]
) -> Iterator[list[T]]:
    # cf. split_before from more-itertools
    chunk: list[T] = []
    for obj in iterable:
        if predicate(obj):
            if chunk:
                yield chunk
            chunk = [obj]
        else:
            chunk.append(obj)
    yield chunk
