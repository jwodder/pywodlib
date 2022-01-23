from typing import Any, Callable
import pytest
from pywodlib.predicate_bsearch import find_first_property, find_last_property


@pytest.mark.parametrize(
    "pred,low,high,x",
    [
        (lambda x: x > 7, 1, 16, 8),
        (lambda x: x > 7, 9, 16, 9),
        (lambda x: x > 7, 1, 9, 8),
    ],
)
def test_find_first_property(
    pred: Callable[[int], Any], low: int, high: int, x: int
) -> None:
    assert find_first_property(pred, low, high) == x


@pytest.mark.parametrize(
    "pred,low,high,x",
    [
        (lambda x: x < 7, 1, 16, 6),
        (lambda x: x < 7, 1, 6, 5),
        (lambda x: x < 7, 6, 16, 6),
    ],
)
def test_find_last_property(
    pred: Callable[[int], Any], low: int, high: int, x: int
) -> None:
    assert find_last_property(pred, low, high) == x
