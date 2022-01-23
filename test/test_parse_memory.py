import pytest
from pywodlib.strings.parse_memory import parse_memory


@pytest.mark.parametrize(
    "iso,numbytes",
    [
        ("42", 42),
        ("42k", 43008),
        ("42 MB", 44040192),
    ],
)
def test_parse_memory(iso: str, numbytes: int) -> None:
    assert parse_memory(iso) == numbytes
