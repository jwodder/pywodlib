from typing import Iterable, Iterator


def yield_lines(fp: Iterable[str]) -> Iterator[str]:
    # Like pkg_resources.yield_lines(), but without the dependency on
    # pkg_resources
    for line in fp:
        line = line.strip()
        if line and not line.startswith("#"):
            yield line
