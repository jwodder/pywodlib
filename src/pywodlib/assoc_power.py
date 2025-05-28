from __future__ import annotations
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def assoc_power(func: Callable[[T, T], T], n: int, x: T) -> T:
    if n < 1:
        raise ValueError("`n` argument must be positive")
    i = 1
    while not (n & i):
        x = func(x, x)
        i <<= 1
    agg = x
    i <<= 1
    x = func(x, x)
    while i <= n:
        if n & i:
            agg = func(agg, x)
        i <<= 1
        x = func(x, x)
    return agg
