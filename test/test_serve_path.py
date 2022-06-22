from pathlib import Path
import pytest
import requests
from pywodlib.serve_path import serve_path

DATA_DIR = Path(__file__).with_name("data")


@pytest.mark.parametrize(
    "bind_address",
    [
        "127.0.0.1",
        "localhost",
        pytest.param(
            "",
            marks=pytest.mark.skip(
                reason="Binding to all addresses runs afoul of macOS security"
            ),
        ),
    ],
)
def test_serve_path(bind_address: str) -> None:
    with serve_path(
        DATA_DIR, bind_address=bind_address
    ) as base_url, requests.Session() as s:
        for p in DATA_DIR.iterdir():
            r = s.get(f"{base_url}/{p.name}")
            r.raise_for_status()
            assert r.content == p.read_bytes()
