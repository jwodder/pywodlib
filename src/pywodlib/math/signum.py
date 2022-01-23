from numbers import Number


def signum(x: Number) -> Number:
    """
    Returns the sign of ``x``: 1 if positive, -1 if negative, 0 if zero.  For
    complex numbers, returns the number with the same phase angle and magnitude
    1.
    """
    return 0 if x == 0 else x / abs(x)
