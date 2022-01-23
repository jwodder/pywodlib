from typing import Any, Callable


def find_first_property(p: Callable[[int], Any], low: int, high: int) -> int:
    """
    Given a range ``(low, high)`` in which there exists an ``x`` such that
    ``not p(i)`` for all ``i`` in ``range(low, x)`` and ``p(i)`` for all ``i``
    in ``range(x, high)``, return ``x``.
    """
    lo = low
    hi = high
    while lo < hi:
        mid = (lo + hi) // 2
        if p(mid):
            if mid > low and p(mid - 1):
                hi = mid
            else:
                return mid
        else:
            lo = mid + 1
    raise AssertionError


def find_last_property(p: Callable[[int], Any], low: int, high: int) -> int:
    """
    Given a range ``(low, high)`` in which there exists an ``x`` such that
    ``p(i)`` for all ``i`` in ``range(low, x+1)`` and ``not p(i)`` for all
    ``i`` in ``range(x+1, high)``, return ``x``.
    """
    lo = low
    hi = high
    while lo < hi:
        mid = (lo + hi) // 2
        if p(mid):
            if mid + 1 < high and p(mid + 1):
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid
    raise AssertionError
