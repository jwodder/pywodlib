import re


def parse_memory(s: str) -> int:
    """
    >>> parse_memory('42')
    42
    >>> parse_memory('42k')
    43008
    >>> parse_memory('42 MB')
    44040192
    """
    m = re.fullmatch(r"(\d+)(?:\s*([kMGTPEZY])B?)?", s)
    if not m:
        raise ValueError(s)
    x = int(m[1])
    if m[2] is not None:
        x <<= 10 * ("kMGTPEZY".index(m[2]) + 1)
    return x
