def strip_suffix(s: str, suffix: str) -> str:
    # cf. str.removesuffix, introduced in Python 3.9
    """
    If ``s`` ends with ``suffix``, return the rest of ``s`` before ``suffix``;
    otherwise, return ``s`` unchanged.

    >>> strip_suffix('foobar', 'bar')
    'foo'
    >>> strip_suffix('foobar', 'foo')
    'foobar'
    >>> strip_suffix('foobar', '')
    'foobar'
    >>> strip_suffix('foobar', 'foobar')
    ''
    >>> strip_suffix('foobar', 'foobarx')
    'foobar'
    >>> strip_suffix('foobar', 'xfoobar')
    'foobar'
    """
    n = len(suffix)
    return s[:-n] if s[-n:] == suffix else s
