import pytest
from pywodlib.math.lcm import lcm


@pytest.mark.parametrize(
    "x,y,z",
    [
        (0, 0, 0),
        (0, 4, 0),
        (4, 0, 0),
        (2, 4, 4),
        (2, 3, 6),
        (6, 4, 12),
        (-6, 4, 12),
        (6, -4, 12),
        (-6, -4, 12),
    ],
)
def test_lcm(x, y, z):
    assert lcm(x, y) == z
