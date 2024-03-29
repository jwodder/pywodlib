from __future__ import annotations
import logging
from pathlib import Path
import shlex
import subprocess
import sys
from typing import Any

log = logging.getLogger(__name__)


def runcmd(*args: str | Path, **kwargs: Any) -> subprocess.CompletedProcess:
    argstrs = [str(a) for a in args]
    log.debug("Running: %s", " ".join(map(shlex.quote, argstrs)))
    r = subprocess.run(argstrs, **kwargs)
    if r.returncode != 0:
        sys.exit(r.returncode)
    return r


def readcmd(*args: str | Path, **kwargs: Any) -> str:
    kwargs["stdout"] = subprocess.PIPE
    kwargs["text"] = True
    r = runcmd(*args, **kwargs)
    assert isinstance(r.stdout, str)
    return r.stdout.strip()
