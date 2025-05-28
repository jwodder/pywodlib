from math import floor, log


def digits(n: int, base: int = 10) -> int:
    """
    Returns the number of digits in the base-``base`` representation of a given
    integer
    """
    if base < 2:
        raise ValueError(f"invalid base: {base!r}")
    if n < 0:
        return digits(-n, base)
    elif n == 0:
        return 1
    else:
        return int(floor(log(n, base))) + 1
