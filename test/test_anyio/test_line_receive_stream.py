from pathlib import Path
import subprocess
import sys
import anyio
from anyio.streams.text import TextReceiveStream
import pytest
from pywodlib.thirdparty.anyio.line_receive_stream import LineReceiveStream

DATA_DIR = Path(__file__).parent.with_name("data")


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.mark.anyio
async def test_line_receive_stream() -> None:
    async with await anyio.open_process(
        [sys.executable, str(DATA_DIR / "printer.py")],
        stdin=None,
        stdout=subprocess.PIPE,
        stderr=None,
    ) as p:
        assert p.stdout is not None
        text_stream = TextReceiveStream(p.stdout)
        async with LineReceiveStream(text_stream) as line_stream:
            lines = [ln async for ln in line_stream]
    assert lines == [
        "This is test text.\n",
        "This is a very, very, very (well, not really) long line.\n",
        "This line ends in a CR.\n",
        "¡Weird!",
    ]
