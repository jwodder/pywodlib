import pytest
from pywodlib.strings.strip_suffix import strip_suffix


@pytest.mark.parametrize(
    "s,suffix,stripped",
    [
        ("foobar", "bar", "foo"),
        ("foobar", "foo", "foobar"),
        ("foobar", "", "foobar"),
        ("foobar", "foobar", ""),
        ("foobar", "foobarx", "foobar"),
        ("foobar", "xfoobar", "foobar"),
    ],
)
def test_strip_suffix(s: str, suffix: str, stripped: str) -> None:
    assert strip_suffix(s, suffix) == stripped
