import pytest

def modinverse(a: int, n: int) -> int:
    """
    ``modinverse(a, n)`` returns the `modular multiplicative inverse`_ of ``a``
    *modulo* ``n``, i.e., the smallest positive integer ``x`` such that ``(a *
    x) % n == 1``.  A `ValueError` is raised if ``a`` is not relatively prime
    to ``n``.

    .. _modular multiplicative inverse:
       https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    Starting in Python 3.8, this function can be replaced with ``pow(a, -1,
    n)``.
    """
    (u, uc) = (abs(n), 0)
    (l, lc) = (a % u, 1)
    while l > 1:
        (u, uc, l, lc) = (l, lc, u % l, uc - lc * (u//l))
    if l == 1:
        return lc % abs(n)
    else:
        raise ValueError(f'{a} has no multiplicative inverse modulo {n}')

@pytest.mark.parametrize('a,n,inv', [
    (3, 5, 2),
    (-2, 5, 2),
    (3, -5, 2),
])
def test_modinverse(a, n, inv):
    assert modinverse(a,n) == inv

@pytest.mark.parametrize('a,n', [
    (2, 6),
    (0, 3),
])
def test_modinverse_error(a,n):
    with pytest.raises(ValueError):
        modinverse(a,n)
