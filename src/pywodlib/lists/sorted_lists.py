from __future__ import annotations
from bisect import bisect_left
from typing import TypeVar

T = TypeVar("T")


def in_sorted_list(xs: list[T], x: T) -> bool:
    # TODO: Add support for cmp & key arguments etc.
    return bool(xs) and x <= xs[-1] and xs[bisect_left(xs, x)] == x  # type: ignore


def insert_uniq(xs: list[T], x: T) -> None:
    # TODO: Add support for cmp & key arguments etc.
    """
    Inserts an element ``x`` into a sorted list ``xs`` if it is not already
    present while maintaining sorted order
    """
    i = bisect_left(xs, x)  # type: ignore
    if not (i < len(xs) and xs[i] == x):
        xs.insert(i, x)
