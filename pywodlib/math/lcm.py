from   math import gcd
import pytest

def lcm(x,y):
    # type: (int, int) -> int
    """
    Calculate the least common (positive) multiple of two integers.  Returns
    zero if either argument is zero.
    """
    d = gcd(x,y)
    return 0 if d == 0 else abs(x*y) // d

@pytest.mark.parametrize('x,y,z', [
    (0, 0, 0),
    (0, 4, 0),
    (4, 0, 0),
    (2, 4, 4),
    (2, 3, 6),
    (6, 4, 12),
    (-6, 4, 12),
    (6, -4, 12),
    (-6, -4, 12),
])
def test_lcm(x,y,z):
    assert lcm(x,y) == z
