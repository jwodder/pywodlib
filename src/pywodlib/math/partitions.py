from __future__ import annotations
from collections.abc import Iterator


def partitions(n: int) -> Iterator[tuple[int, ...]]:
    """
    Yield all partitions of ``n`` unlabelled objects into any number of
    unlabelled nonempty bins.

    >>> list(partitions(5))
    [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
    """

    def gen(qty: int, mx: int) -> Iterator[tuple[int, ...]]:
        if qty == 0:
            yield ()
        else:
            for i in range(min(qty, mx), 0, -1):
                for xs in gen(qty - i, i):
                    yield (i,) + xs

    if n < 1:
        raise ValueError(n)
    else:
        return gen(n, n)
