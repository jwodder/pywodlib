from typing import Iterator, Optional


def exp_wait(
    base: float = 1.25,
    multiplier: float = 1,
    attempts: Optional[int] = None,
) -> Iterator[float]:
    # cf. `itersleep_exponential()`
    """
    Returns a generator of values usable as `sleep()` times when retrying
    something with exponential backoff.

    :param float base:
    :param float multiplier: value to multiply values by after exponentiation
    :param Optional[int] attempts: how many values to yield; set to `None` to
        yield forever
    :rtype: Iterator[float]
    """
    n = 0
    while attempts is None or n < attempts:
        yield base ** n * multiplier
        n += 1
