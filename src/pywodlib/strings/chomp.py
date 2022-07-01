def chomp(s: str) -> str:
    """Remove a trailing LF, CR LF, or CR from ``s``, if any"""
    if s.endswith("\n"):
        s = s[:-1]
    if s.endswith("\r"):
        s = s[:-1]
    return s
