from math import gcd


def lcm(x: int, y: int) -> int:
    # cf. math.lcm(), introduced in Python 3.9
    """
    Calculate the least common (positive) multiple of two integers.  Returns
    zero if either argument is zero.
    """
    d = gcd(x, y)
    return 0 if d == 0 else abs(x * y) // d
