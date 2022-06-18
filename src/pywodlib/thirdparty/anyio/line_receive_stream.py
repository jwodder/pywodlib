from typing import Optional
from anyio import EndOfStream
from anyio.abc import ObjectReceiveStream
from linesep import SplitterEmptyError, get_newline_splitter


class LineReceiveStream(ObjectReceiveStream[str]):
    def __init__(
        self, transport_stream: ObjectReceiveStream[str], newline: Optional[str] = None
    ) -> None:
        self._stream = transport_stream
        self._splitter = get_newline_splitter(newline, retain=True)

    async def receive(self) -> str:
        while not self._splitter.nonempty and not self._splitter.closed:
            try:
                self._splitter.feed(await self._stream.receive())
            except EndOfStream:
                self._splitter.close()
        try:
            return self._splitter.get()
        except SplitterEmptyError:
            raise EndOfStream()

    async def aclose(self) -> None:
        await self._stream.aclose()
