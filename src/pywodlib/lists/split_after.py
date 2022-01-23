from typing import Any, Callable, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def split_after(
    predicate: Callable[[T], Any], iterable: Iterable[T]
) -> Iterator[List[T]]:
    # cf. split_after from more-itertools
    empty = True
    chunk: List[T] = []
    for obj in iterable:
        empty = False
        chunk.append(obj)
        if predicate(obj):
            yield chunk
            chunk = []
    if empty or chunk:
        yield chunk
