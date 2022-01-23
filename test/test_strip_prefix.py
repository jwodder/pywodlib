import pytest
from pywodlib.strings.strip_prefix import strip_prefix


@pytest.mark.parametrize(
    "s,prefix,stripped",
    [
        ("foobar", "foo", "bar"),
        ("foobar", "bar", "foobar"),
        ("foobar", "", "foobar"),
        ("foobar", "foobar", ""),
        ("foobar", "foobarx", "foobar"),
        ("foobar", "xfoobar", "foobar"),
    ],
)
def test_strip_prefix(s: str, prefix: str, stripped: str) -> None:
    assert strip_prefix(s, prefix) == stripped
