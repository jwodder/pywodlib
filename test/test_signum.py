from __future__ import annotations
import pytest
from pywodlib.math.signum import signum


@pytest.mark.parametrize(
    "num,sign",
    [
        (0, 0),
        (-42, -1.0),
        (23, 1.0),
        (5j, 1j),
        (-6j, -0 - 1j),
        (3 + 4j, 0.6 + 0.8j),
    ],
)
def test_signum(num: float | complex, sign: float | complex) -> None:
    assert signum(num) == sign
