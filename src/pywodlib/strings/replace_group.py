from __future__ import annotations
from collections import Callable
import re


def replace_group(
    rgx: str | re.Pattern[str],
    replacer: Callable[[str], str],
    s: str,
    group: int | str = 1,
) -> str:
    """
    If the regex ``rgx`` is found in ``s``, replace the contents ``t`` of the
    group ``group`` in ``s`` with ``replacer(t)``
    """
    m = re.search(rgx, s)
    if m:
        s = s[: m.start(group)] + replacer(m[group]) + s[m.end(group) :]
    return s
