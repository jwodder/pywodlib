"""
`ReSubProcess` evaluates function calls by passing values off to a
continuously-running subprocess which is restarted if it crashes.  It takes a
class (which must be a context manager that returns a callable on entry) & a
collection of constructor arguments and starts a subprocess in which an
instance of the class is constructed with the given arguments, the instance's
context is entered, and the callable returned on entry is used to evaluate
function calls passed from the calling process.

Usage::

    with ReSubProcess(cls, args=..., kwargs=...) as rsp:
        for x in ...:
            y = rsp(x)
"""

from __future__ import annotations
from dataclasses import dataclass, field
import logging
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection
from signal import SIGINT
from typing import Any, Optional, Sequence

__all__ = ["ReSubProcess"]

log = logging.getLogger(__name__)


@dataclass
class ReSubProcess:
    target: Any
    args: Sequence = ()
    kwargs: dict = field(default_factory=dict)
    max_tries: Optional[int] = None
    process: Optional[Process] = field(init=False, default=None)
    pipe: Optional[Connection] = field(init=False, default=None)

    def __enter__(self) -> ReSubProcess:
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        i = 0
        while True:
            self._ensure()
            log.debug("Sending args=%r, kwargs=%r to subprocess", args, kwargs)
            assert self.pipe is not None
            self.pipe.send((args, kwargs))
            try:
                log.debug("Reading from subprocess")
                r = self.pipe.recv()
                log.debug("Subprocess sent back %r", r)
            except EOFError:
                i += 1
                if self.max_tries is not None and i >= self.max_tries:
                    raise RuntimeError("Subprocess failed too many times; giving up")
                log.warning(
                    "Subprocess exited while processing args=%r, kwargs=%r; restarting",
                    args,
                    kwargs,
                )
                log.debug("Waiting for subprocess to terminate ...")
                assert self.process is not None
                self.process.join()
                log.debug("Subprocess terminated")
                continue
            return r

    def _ensure(self) -> None:
        if self.process is None:
            log.debug("Starting subprocess")
            self._start()
        elif not self.process.is_alive():
            if self.process.exitcode == -SIGINT:
                raise KeyboardInterrupt("Child process received Cntrl-C")
            log.debug("Subprocess is dead; restarting")
            self.process.close()
            self._start()

    def _start(self) -> None:
        self.pipe, subpipe = Pipe()
        self.process = Process(
            target=subproc,
            args=(self.target, self.args, self.kwargs, self.pipe, subpipe),
        )
        self.process.start()
        subpipe.close()

    def close(self) -> None:
        if self.process is not None:
            assert self.pipe is not None
            self.pipe.close()
            if self.process.is_alive():
                log.debug("Terminating subprocess")
                self.process.terminate()
                self.process.join(2)  ### TODO: Make this time configurable
                if self.process.is_alive():
                    log.debug("Subprocess did not exit in time; killing")
                    self.process.kill()
            self.process.close()
            self.process = None
            self.pipe = None


def subproc(
    cls: type, args: Sequence, kwargs: dict, p1: Connection, pipe: Connection
) -> None:
    p1.close()  # <https://stackoverflow.com/a/6567318/744178>
    with cls(*args, **kwargs) as func:
        while True:
            try:
                c_args, c_kwargs = pipe.recv()
            except EOFError:
                break
            r = func(*c_args, **c_kwargs)
            pipe.send(r)
