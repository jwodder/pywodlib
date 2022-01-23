from typing import Any, Callable, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


def split_before(
    predicate: Callable[[T], Any], iterable: Iterable[T]
) -> Iterator[List[T]]:
    # cf. split_before from more-itertools
    chunk = []
    for obj in iterable:
        if predicate(obj):
            if chunk:
                yield chunk
            chunk = [obj]
        else:
            chunk.append(obj)
    yield chunk
