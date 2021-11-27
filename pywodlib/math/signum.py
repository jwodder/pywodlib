from numbers import Number


def signum(x: Number) -> Number:
    """
    Returns the sign of ``x``: 1 if positive, -1 if negative, 0 if zero.  For
    complex numbers, returns the number with the same phase angle and magnitude
    1.

    >>> signum(0)
    0
    >>> signum(-42)
    -1.0
    >>> signum(23)
    1.0
    >>> signum(5j)
    1j
    >>> signum(-6j)
    (-0-1j)
    >>> signum(3+4j)
    (0.6+0.8j)
    """
    return 0 if x == 0 else x / abs(x)
