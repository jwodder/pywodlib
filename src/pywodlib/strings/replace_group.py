import re
from typing import Callable, Pattern, Union


def replace_group(
    rgx: Union[str, Pattern[str]],
    replacer: Callable[[str], str],
    s: str,
    group: Union[int, str] = 1,
) -> str:
    m = re.search(rgx, s)
    if m:
        s = s[: m.start(group)] + replacer(m[group]) + s[m.end(group) :]
    return s
