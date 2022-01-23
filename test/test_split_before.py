from typing import Any, Callable, List
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
    pred: Callable[[int], Any], xs: List[int], split: List[List[int]]
) -> None:
    assert list(split_before(pred, xs)) == split
