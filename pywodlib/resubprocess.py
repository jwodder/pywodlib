"""
`ReSubProcess` spawns a subprocess in which calls to a given function (or
callable class) are evaluated; if the subprocess crashes, it is restarted.

Usage::

    with ReSubProcess(cls_or_callable, args=..., kwargs=...) as rsp:
        for x in ...:
            y = rsp(x)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from inspect import isclass
import logging
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection
from typing import Any, Callable, Optional, Sequence

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

    def __call__(self, *args, **kwargs):
        i = 0
        while True:
            self._ensure()
            log.debug("Sending args=%r, kwargs=%r to subprocess", args, kwargs)
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
                self.process.join()
                log.debug("Subprocess terminated")
                continue
            return r

    def _ensure(self):
        if self.process is None:
            log.info("Starting subprocess")
            self._start()
        elif not self.process.is_alive():
            log.info("Subprocess is dead; restarting")
            self.process.close()
            self._start()

    def _start(self):
        self.pipe, subpipe = Pipe()
        if isclass(self.target):
            t = cls_subproc
        elif callable(self.target):
            t = func_subproc
        else:
            raise TypeError("Target must be a class or callable")
        self.process = Process(
            target=t, args=(self.target, self.args, self.kwargs, self.pipe, subpipe)
        )
        self.process.start()
        subpipe.close()

    def close(self):
        if self.process is not None:
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


def cls_subproc(
    cls: type, args: Sequence, kwargs: dict, p1: Connection, pipe: Connection
) -> None:
    p1.close()  # <https://stackoverflow.com/a/6567318/744178>
    obj = cls(*args, **kwargs)
    try:
        while True:
            try:
                c_args, c_kwargs = pipe.recv()
            except EOFError:
                break
            r = obj(*c_args, **c_kwargs)
            pipe.send(r)
    finally:
        if hasattr(obj, "close"):
            obj.close()


def func_subproc(
    func: Callable, args: Sequence, kwargs: dict, p1: Connection, pipe: Connection
) -> None:
    p1.close()  # <https://stackoverflow.com/a/6567318/744178>
    while True:
        try:
            c_args, c_kwargs = pipe.recv()
        except EOFError:
            break
        r = func(*args, *c_args, **kwargs, **c_kwargs)
        pipe.send(r)
