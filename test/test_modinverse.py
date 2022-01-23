import pytest
from pywodlib.math.modinverse import modinverse


@pytest.mark.parametrize(
    "a,n,inv",
    [
        (3, 5, 2),
        (-2, 5, 2),
        (3, -5, 2),
    ],
)
def test_modinverse(a, n, inv):
    assert modinverse(a, n) == inv


@pytest.mark.parametrize(
    "a,n",
    [
        (2, 6),
        (0, 3),
    ],
)
def test_modinverse_error(a, n):
    with pytest.raises(ValueError):
        modinverse(a, n)
