from __future__ import annotations
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def fragment(xs: Sequence[T], n: int) -> list[list[T]]:
    # cf. chunked from more-itertools
    # cf. itertools.batched() in Python 3.12+
    """
    Split a sequence into subsequences of length ``n`` (except possibly the
    last subsequence)
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    return [list(xs[i : i + n]) for i in range(0, len(xs), n)]
