import pytest
from pywodlib.strings.qqrepr import qqrepr


@pytest.mark.parametrize(
    "ins,outs",
    [
        ("foo", '"foo"'),
        ("they're", '"they\'re"'),
        ('"Beware the Jabberwock, my son!"', '"\\"Beware the Jabberwock, my son!\\""'),
    ],
)
def test_qqrepr(ins: str, outs: str) -> None:
    assert qqrepr(ins) == outs
