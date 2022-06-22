from __future__ import annotations
from collections.abc import Iterator
from contextlib import contextmanager
from subprocess import Popen


@contextmanager
def kill_on_error(p: Popen, timeout: float = 5) -> Iterator[Popen]:
    """
    When used like so::

        with kill_on_error(subprocess.Popen(...), timeout=...) as p:
            ...

    then the subprocess ``p``, in addition to being waited for on normal
    context manager exit, will be terminated if an error occurs in the body of
    the ``with:`` block; if it doesn't exit after ``timeout`` seconds, it will
    instead be killed.
    """

    with p:
        try:
            yield p
        except BaseException:
            p.terminate()
            try:
                p.wait(timeout)
            except TimeoutError:
                p.kill()
            raise
