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
def test_modinverse(a: int, n: int, inv: int) -> None:
    assert modinverse(a, n) == inv


@pytest.mark.parametrize(
    "a,n",
    [
        (2, 6),
        (0, 3),
    ],
)
def test_modinverse_error(a: int, n: int) -> None:
    with pytest.raises(ValueError):
        modinverse(a, n)
