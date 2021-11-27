from typing import List
import pytest


def comma_split(s: str) -> List[str]:
    """
    Split apart a string on commas, discarding leading & trailing whitespace
    from all parts and discarding empty parts
    """
    return [k for k in map(str.strip, s.split(",")) if k]


@pytest.mark.parametrize(
    "sin,lout",
    [
        ("", []),
        (" ", []),
        (",", []),
        (" , ", []),
        (" , , ", []),
        ("foo", ["foo"]),
        ("foo,bar", ["foo", "bar"]),
        ("foo, bar", ["foo", "bar"]),
        ("foo ,bar", ["foo", "bar"]),
        (" foo , bar ", ["foo", "bar"]),
        (" foo , , bar ", ["foo", "bar"]),
        ("foo,,bar", ["foo", "bar"]),
        ("foo bar", ["foo bar"]),
        (",foo", ["foo"]),
        ("foo,", ["foo"]),
    ],
)
def test_comma_split(sin, lout):
    assert comma_split(sin) == lout
