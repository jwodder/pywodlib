def split_before(predicate, iterable):
    """
    >>> list(split_before(lambda n: n % 2, [2, 4, 1, 6, 8, 3]))
    [[2, 4], [1, 6, 8], [3]]
    >>> list(split_before(lambda n: n % 2, [5, 2, 4, 1, 6, 8, 3]))
    [[5, 2, 4], [1, 6, 8], [3]]
    >>> list(split_before(lambda n: n % 2, [2, 4, 1, 6, 8]))
    [[2, 4], [1, 6, 8]]
    >>> list(split_before(lambda n: n % 2, [2, 4, 6, 8]))
    [[2, 4, 6, 8]]
    >>> list(split_before(lambda n: n % 2, []))
    [[]]
    >>> list(split_before(lambda n: n % 2, [2, 4, 1, 5, 6, 8, 3]))
    [[2, 4], [1], [5, 6, 8], [3]]
    >>> list(split_before(lambda n: n % 2, [1]))
    [[1]]
    >>> list(split_before(lambda n: n % 2, [1, 5, 3]))
    [[1], [5], [3]]
    """
    chunk = []
    for obj in iterable:
        if predicate(obj):
            if chunk:
                yield chunk
            chunk = [obj]
        else:
            chunk.append(obj)
    yield chunk
