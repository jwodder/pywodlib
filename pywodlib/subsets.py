from itertools import compress

def subsets(xs, nonempty=False, proper=False):
    """
    Returns an iterator over all subsets of the iterable ``xs`` as tuples.  If
    ``nonempty`` is true, only nonempty subsets are returned.  If ``proper`` is
    true, only proper subsets are returned.
    """
    xs = tuple(xs)
    selectors = [False] * len(xs)
    while True:
        if not (
            (nonempty and not any(selectors)) or (proper and all(selectors))
        ):
            yield tuple(compress(xs, selectors))
        for i in xrange(len(selectors)):
            selectors[i] = not selectors[i]
            if selectors[i]:
                break
        else:
            break
