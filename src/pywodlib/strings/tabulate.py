from __future__ import annotations
from collections.abc import Sequence


def tabulate(cells: Sequence[Sequence[str]], gutter_width: int = 2) -> str:
    """
    Show a bare-bones table of values, with no borders or other stylings.

    All rows in ``cells`` must be the same length.
    """
    colwidths = [max(map(len, col)) for col in zip(*cells)]
    lines = [
        (" " * gutter_width).join(c.ljust(w) for c, w in zip(row, colwidths))
        for row in cells
    ]
    return "\n".join(lines)
