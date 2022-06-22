from __future__ import annotations
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
import anyio


@asynccontextmanager
async def kill_on_error(
    p: anyio.abc.Process, timeout: float = 5
) -> AsyncIterator[anyio.abc.Process]:

    """
    When used like so::

        async with kill_on_error(await anyio.open_process(...), timeout=...) as p:
            ...

    then the subprocess ``p``, in addition to being waited for on normal
    context manager exit, will be terminated if an error occurs in the body of
    the ``async with:`` block; if it doesn't exit after ``timeout`` seconds, it
    will instead be killed.
    """

    async with p:
        try:
            yield p
        except BaseException:
            with anyio.CancelScope(shield=True):
                p.terminate()
                try:
                    with anyio.fail_after(timeout):
                        await p.wait()
                except TimeoutError:
                    p.kill()
            raise
