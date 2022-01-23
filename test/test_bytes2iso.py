import pytest
from pywodlib.bytes2iso import bytes2iso


@pytest.mark.parametrize(
    "numbytes,iso",
    [
        (512, "512 B"),
        (1024, "1.00 kB"),
        (1000000, "976.56 kB"),
        (2334597576389, "2.12 TB"),
        (1208925819614629174706176000000, "1000000.00 YB"),
    ],
)
def test_bytes2iso(numbytes: int, iso: str) -> None:
    assert bytes2iso(numbytes) == iso
