def strip_prefix(s, prefix):
    # type: (str, str) -> str
    # cf. str.removeprefix, introduced in Python 3.9
    """
    If ``s`` starts with ``prefix``, return the rest of ``s`` after ``prefix``;
    otherwise, return ``s`` unchanged.

    >>> strip_prefix('foobar', 'foo')
    'bar'
    >>> strip_prefix('foobar', 'bar')
    'foobar'
    >>> strip_prefix('foobar', '')
    'foobar'
    >>> strip_prefix('foobar', 'foobar')
    ''
    >>> strip_prefix('foobar', 'foobarx')
    'foobar'
    >>> strip_prefix('foobar', 'xfoobar')
    'foobar'
    """
    n = len(prefix)
    return s[n:] if s[:n] == prefix else s
