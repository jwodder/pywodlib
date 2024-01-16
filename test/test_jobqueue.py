from __future__ import annotations
from collections.abc import Iterator
import os
from pathlib import Path
from interleave import interleave
from pywodlib.jobqueue import JobStack


def test_jobstack_threaded_iterpath(tmp_path: Path) -> None:
    LAYOUT = (8, 10, 12, 16)
    WORKERS = min(32, (os.cpu_count() or 1) + 4)

    paths = set()
    dirs = [tmp_path]
    for i, width in enumerate(LAYOUT):
        if i < len(LAYOUT) - 1:
            dirs2 = []
            for d in dirs:
                for x in range(width):
                    d2 = d / f"d{x}"
                    d2.mkdir()
                    dirs2.append(d2)
            dirs = dirs2
        else:
            for d in dirs:
                for x in range(width):
                    f = d / f"f{x}.dat"
                    f.touch()
                    paths.add(f)

    jobqueue = JobStack([tmp_path])

    def worker() -> Iterator[Path]:
        for ctx in jobqueue:
            with ctx as dirpath:
                for p in dirpath.iterdir():
                    if p.is_dir():
                        jobqueue.put(p)  # noqa: B038
                    else:
                        yield p

    with interleave([worker() for _ in range(WORKERS)], max_workers=WORKERS) as it:
        assert paths == set(it)
