def int_sqrt(n: int) -> int:
    """
    Returns the floor of the square root of an integral value *exactly*.  Based
    on <https://wiki.haskell.org/Generic_number_type#squareRoot>.

    cf. `math.isqrt()` in Python 3.8+
    """
    if n < 0:
        raise ValueError("negative argument")
    elif n < 2:
        return n
    else:
        (a, b) = (1, 2)
        while n >= b * b:
            (a, b) = (b, b * b)
        x = int_sqrt(n // b) * a
        while not (x * x <= n < (x + 1) * (x + 1)):
            x = (x + n // x) // 2
        return x
