from __future__ import annotations


def comma_split(s: str) -> list[str]:
    """
    Split apart a string on commas, discarding leading & trailing whitespace
    from all parts and discarding empty parts
    """
    return [k for k in map(str.strip, s.split(",")) if k]
