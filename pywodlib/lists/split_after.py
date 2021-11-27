def split_after(predicate, iterable):
    # cf. split_after from more-itertools
    """
    >>> list(split_after(lambda n: n % 2, [2, 4, 1, 6, 8, 3]))
    [[2, 4, 1], [6, 8, 3]]
    >>> list(split_after(lambda n: n % 2, [5, 2, 4, 1, 6, 8, 3]))
    [[5], [2, 4, 1], [6, 8, 3]]
    >>> list(split_after(lambda n: n % 2, [2, 4, 1, 6, 8]))
    [[2, 4, 1], [6, 8]]
    >>> list(split_after(lambda n: n % 2, [2, 4, 6, 8]))
    [[2, 4, 6, 8]]
    >>> list(split_after(lambda n: n % 2, []))
    [[]]
    >>> list(split_after(lambda n: n % 2, [2, 4, 1, 5, 6, 8, 3]))
    [[2, 4, 1], [5], [6, 8, 3]]
    >>> list(split_after(lambda n: n % 2, [1]))
    [[1]]
    >>> list(split_after(lambda n: n % 2, [1, 5, 3]))
    [[1], [5], [3]]
    """
    empty = True
    chunk = []
    for obj in iterable:
        empty = False
        chunk.append(obj)
        if predicate(obj):
            yield chunk
            chunk = []
    if empty or chunk:
        yield chunk
