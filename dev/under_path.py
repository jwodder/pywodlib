from __future__ import annotations
import os
from pathlib import Path


def under_path(p1: str | os.PathLike[str], p2: str | os.PathLike[str]) -> bool:
    """
    Returns true iff ``p1`` (which must exist) is a path at or under the
    directory hierarchy at ``p2`` (which may or may not exist), without
    following any symlinks under ``p2``.  Specifically, this answers the
    question, "If one runs ``rm -rf p2`` (after resolving trailing ``..``'s),
    will ``p1`` cease to exist?"
    """

    ### TODO: Hammer out the exact semantics for p2 paths that end with .. or .
    ### (which rm rejects and shutil.rmtree() does the wrong thing on before
    ### erroring), especially when the component before that is a symlink

    p1 = Path(p1).resolve()
    p2 = Path(p2).resolve()
    try:
        p1.relative_to(p2)
    except ValueError:
        return False
    else:
        return True
