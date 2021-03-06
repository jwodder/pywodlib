from __future__ import annotations
import pytest
from pywodlib.strings.comma_split import comma_split


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
def test_comma_split(sin: str, lout: list[str]) -> None:
    assert comma_split(sin) == lout
