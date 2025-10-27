import pytest
from pywodlib.strings.unescape import unescape


@pytest.mark.parametrize(
    "src,dest",
    [
        ("foo", "foo"),
        (r"foo\n", "foo\n"),
        (r"foo\\n", "foo\\n"),
        (r"foo\\\n", "foo\\\n"),
        (r"foo\012", "foo\n"),
        (r"foo\x0A", "foo\n"),
        (r"foo\u000A", "foo\n"),
        (r"foo\\bar", r"foo\bar"),
        (r"foo\'bar", "foo'bar"),
        (r"foo\"bar", 'foo"bar'),
        (r"foo\abar", "foo\abar"),
        (r"foo\bbar", "foo\bbar"),
        (r"foo\fbar", "foo\fbar"),
        (r"foo\rbar", "foo\rbar"),
        (r"foo\tbar", "foo\tbar"),
        (r"foo\vbar", "foo\vbar"),
        (r"\U0001F410", "\U0001f410"),
        ("åéîøü", "åéîøü"),
        (r"\u2603", "\u2603"),
        ("\u2603", "\u2603"),
        ("\U0001f410", "\U0001f410"),
        (r"\N{SNOWMAN}", "\u2603"),
    ],
)
def test_unescape(src: str, dest: str) -> None:
    assert unescape(src) == dest
