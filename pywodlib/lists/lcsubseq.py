"""
Functions for finding the longest common subsequence (or length thereof) of two
iterables.  Note that the elements of the subsequence need not be consecutive
in the original iterables; if they are required to be consecutive, this instead
becomes the longest common *substring* problem.
"""

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def _lcs_table(xs: List[T], ys: List[T]) -> List[List[int]]:
    tbl = [[0] * (len(ys) + 1) for _ in range(len(xs) + 1)]
    for i in range(len(xs)):
        for j in range(len(ys)):
            if xs[i] == ys[j]:
                tbl[i + 1][j + 1] = tbl[i][j] + 1
            else:
                tbl[i + 1][j + 1] = max(tbl[i + 1][j], tbl[i][j + 1])
    return tbl


def longest_common_subseq_len(xs: Sequence[T], ys: Sequence[T]) -> int:
    """
    >>> longest_common_subseq_len('XMJYAUZ', 'MZJAWXU')
    4
    """
    return _lcs_table(list(xs), list(ys))[-1][-1]


def longest_common_subseq(xs: Sequence[T], ys: Sequence[T]) -> List[T]:
    """
    >>> longest_common_subseq('XMJYAUZ', 'MZJAWXU')
    ['M', 'J', 'A', 'U']
    """
    xs = list(xs)
    ys = list(ys)
    tbl = _lcs_table(xs, ys)
    longest = []
    i = len(xs) - 1
    j = len(ys) - 1
    while i >= 0 and j >= 0:
        if xs[i] == ys[j]:
            longest.append(xs[i])
            i -= 1
            j -= 1
        elif tbl[i + 1][j] > tbl[i][j + 1]:
            j -= 1
        else:
            i -= 1
    longest.reverse()
    return longest
