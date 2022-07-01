from __future__ import annotations
from collections.abc import Iterator
import time
from typing import Optional


def itersleep(
    interval: float, maxtime: Optional[float] = None, yield_first: bool = False
) -> Iterator[None]:
    if yield_first:
        yield
    if maxtime is None:
        while True:
            # TODO: Subtract the time since the last `yield` from `interval`???
            time.sleep(interval)
            yield
    else:
        end_time = time.monotonic() + maxtime
        while True:
            time_left = end_time - time.monotonic()
            if time_left <= 0:
                return
            # TODO: Subtract the time since the last `yield` from `interval`???
            time.sleep(min(interval, time_left))
            yield
