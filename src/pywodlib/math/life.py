from __future__ import annotations
from collections import Counter
from collections.abc import Iterable


def life(before: Iterable[tuple[int, int]]) -> set[tuple[int, int]]:
    """
    Takes as input a state of Conway's Game of Life, represented as an iterable
    of ``(int, int)`` pairs giving the coordinates of living cells, and returns
    a `set` of ``(int, int)`` pairs representing the next state
    """
    before = set(before)
    neighbor_qtys = Counter(
        (x + i, y + j)
        for (x, y) in before
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        if (i, j) != (0, 0)
    )
    return {
        xy for (xy, n) in neighbor_qtys.items() if n == 3 or (n == 2 and xy in before)
    }
