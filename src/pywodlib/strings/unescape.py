def unescape(s: str) -> str:
    # <https://stackoverflow.com/a/57192592/744178>
    return s.encode("latin-1", "backslashreplace").decode("unicode_escape")
