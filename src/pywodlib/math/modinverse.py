def modinverse(a: int, n: int) -> int:
    """
    ``modinverse(a, n)`` returns the `modular multiplicative inverse`__ of
    ``a`` *modulo* ``n``, i.e., the smallest positive integer ``x`` such that
    ``(a * x) % n == 1``.  A `ValueError` is raised if ``a`` is not relatively
    prime to ``n``.

    __ https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    Starting in Python 3.8, this function can be replaced with ``pow(a, -1,
    n)``.
    """
    (upper, uc) = (abs(n), 0)
    (lower, lc) = (a % upper, 1)
    while lower > 1:
        (upper, uc, lower, lc) = (lower, lc, upper % lower, uc - lc * (upper // lower))
    if lower == 1:
        return lc % abs(n)
    else:
        raise ValueError(f"{a} has no multiplicative inverse modulo {n}")
