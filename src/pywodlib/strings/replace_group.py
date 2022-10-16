from __future__ import annotations
from collections.abc import Callable
import re


def replace_group(
    rgx: str | re.Pattern[str],
    replacer: str | Callable[[str], str],
    s: str,
    group: int | str = 1,
) -> str:
    """
    If the regex ``rgx`` is found in ``s``, replace the contents ``t`` of the
    group ``group`` in ``s`` with ``replacer`` (if it is a string) or
    ``replacer(t)`` (if it is a callable)
    """
    m = re.search(rgx, s)
    if m:
        if isinstance(replacer, str):
            repl = replacer
        else:
            repl = replacer(m[group])
        s = s[: m.start(group)] + repl + s[m.end(group) :]
    return s
