from __future__ import annotations
import pytest
from pywodlib.strings.chomp import chomp


@pytest.mark.parametrize(
    "s,chomped",
    [
        ("", ""),
        ("\n", ""),
        ("\r", ""),
        ("\r\n", ""),
        ("\n\n", "\n"),
        ("foobar", "foobar"),
        ("foobar\n", "foobar"),
        ("foobar\r\n", "foobar"),
        ("foobar\r", "foobar"),
        ("foobar\n\r", "foobar\n"),
        ("foobar\n\n", "foobar\n"),
        ("foobar\nbaz", "foobar\nbaz"),
        ("\nbar", "\nbar"),
    ],
)
def test_chomp(s: str, chomped: str) -> None:
    assert chomp(s) == chomped
