from __future__ import annotations
from dataclasses import dataclass
from types import TracebackType
from psutil import Process
from pywodlib.subprocesses.resubprocess import ReSubProcess


@dataclass
class FlakyDoubler:
    error_on: int
    i: int = 0

    def __enter__(self) -> FlakyDoubler:
        return self

    def __exit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc_val: BaseException | None,
        _exc_tb: TracebackType | None,
    ) -> None:
        return None

    def __call__(self, x: int) -> int:
        self.i += 1
        if self.i >= self.error_on:
            raise RuntimeError("Dying")
        return x * 2


def test_resubprocess() -> None:
    with ReSubProcess(FlakyDoubler, args=(3,)) as rsp:
        for i in range(10):
            assert rsp(i) == 2 * i
    # Python's multiprocessing spawns a special "resource_tracker" process for
    # cleaning up pipes etc., so we need to not count it when checking that all
    # children created by ReSubProcess are gone.
    subcmds = [p.cmdline() for p in Process().children()]
    assert [
        cl for cl in subcmds if not any("resource_tracker" in arg for arg in cl)
    ] == []
