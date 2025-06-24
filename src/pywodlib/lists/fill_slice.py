from __future__ import annotations
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def fill_slice(
    iterable: Iterable[T], width: int, fill: T | None = None
) -> list[T | None]:
    """
    Return the first ``width`` elements of ``iterable`` as a list.  If
    ``iterable`` has fewer than ``width`` elements, the list is padded with
    ``fill`` to make up the difference.
    """
    xs = list(iterable)
    if len(xs) <= width:
        return xs + [fill] * (width - len(xs))
    else:
        return xs[:width]  # type: ignore[return-value]
