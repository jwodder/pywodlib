def find_first_property(p, low, high):
    """
    Given a range ``(low, high)`` in which there exists an ``x`` such that
    ``not p(i)`` for all ``i`` in ``range(low, x)`` and ``p(i)`` for all ``i``
    in ``range(x, high)``, return ``x``.

    >>> find_first_property(lambda x: x > 7, 1, 16)
    8
    >>> find_first_property(lambda x: x > 7, 9, 16)
    9
    >>> find_first_property(lambda x: x > 7, 1, 9)
    8
    """
    l = low
    h = high
    while l < h:
        mid = (l + h) // 2
        if p(mid):
            if mid > low and p(mid-1):
                h = mid
            else:
                return mid
        else:
            l = mid + 1
    assert False

def find_last_property(p, low, high):
    """
    Given a range ``(low, high)`` in which there exists an ``x`` such that
    ``p(i)`` for all ``i`` in ``range(low, x+1)`` and ``not p(i)`` for all
    ``i`` in ``range(x+1, high)``, return ``x``.

    >>> find_last_property(lambda x: x < 7, 1, 16)
    6
    >>> find_last_property(lambda x: x < 7, 1, 6)
    5
    >>> find_last_property(lambda x: x < 7, 6, 16)
    6
    """
    l = low
    h = high
    while l < h:
        mid = (l + h) // 2
        if p(mid):
            if mid+1 < high and p(mid+1):
                l = mid + 1
            else:
                return mid
        else:
            h = mid
    assert False
