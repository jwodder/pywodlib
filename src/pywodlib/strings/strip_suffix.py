def strip_suffix(s: str, suffix: str) -> str:
    # cf. str.removesuffix, introduced in Python 3.9
    """
    If ``s`` ends with ``suffix``, return the rest of ``s`` before ``suffix``;
    otherwise, return ``s`` unchanged.
    """
    n = len(suffix)
    return s[:-n] if s[-n:] == suffix else s
