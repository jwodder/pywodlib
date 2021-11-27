from typing import List, Sequence, TypeVar

T = TypeVar("T")


def fragment(xs: Sequence[T], n: int) -> List[List[T]]:
    # cf. chunked from more-itertools
    if n < 1:
        raise ValueError("n must be at least 1")
    return [xs[i : i + n] for i in range(0, len(xs), n)]
