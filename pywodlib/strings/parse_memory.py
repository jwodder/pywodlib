import re


def parse_memory(s):
    """
    >>> parse_memory('42')
    42
    >>> parse_memory('42k')
    43008
    >>> parse_memory('42 MB')
    44040192
    """
    m = re.match(r"^(\d+)(?:\s*([kMGTPE])B?)?$", s)
    if not m:
        raise ValueError(s)
    x = int(m.group(1))
    if m.group(2) is not None:
        x <<= 10 * ("kMGTPE".index(m.group(2)) + 1)
    return x
