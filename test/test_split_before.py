from __future__ import annotations
from collections.abc import Callable
from typing import Any
import pytest
from pywodlib.lists.split_before import split_before


@pytest.mark.parametrize(
    "pred,xs,split",
    [
        (lambda n: n % 2, [2, 4, 1, 6, 8, 3], [[2, 4], [1, 6, 8], [3]]),
        (lambda n: n % 2, [5, 2, 4, 1, 6, 8, 3], [[5, 2, 4], [1, 6, 8], [3]]),
        (lambda n: n % 2, [2, 4, 1, 6, 8], [[2, 4], [1, 6, 8]]),
        (lambda n: n % 2, [2, 4, 6, 8], [[2, 4, 6, 8]]),
        (lambda n: n % 2, [], [[]]),
        (lambda n: n % 2, [2, 4, 1, 5, 6, 8, 3], [[2, 4], [1], [5, 6, 8], [3]]),
        (lambda n: n % 2, [1], [[1]]),
        (lambda n: n % 2, [1, 5, 3], [[1], [5], [3]]),
    ],
)
def test_split_before(
    pred: Callable[[int], Any], xs: list[int], split: list[list[int]]
) -> None:
    assert list(split_before(pred, xs)) == split
