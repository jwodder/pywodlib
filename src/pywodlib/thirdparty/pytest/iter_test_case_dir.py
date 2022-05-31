import json
from pathlib import Path
from typing import Iterator
from _pytest.mark import ParameterSet
import pytest


def iter_test_case_dir(
    dirpath: Path, inext: str = ".in", outext: str = ".out"
) -> Iterator[ParameterSet]:
    for p in sorted(dirpath.glob("*{inext}")):
        with p.open(encoding="utf-8") as fp:
            if inext == ".json":
                indata = json.load(fp)
            else:
                indata = fp.read()
        with p.with_suffix(outext).open(encoding="utf-8") as fp:
            if outext == ".json":
                outdata = json.load(fp)
            else:
                outdata = fp.read()
        yield pytest.param(indata, outdata, id=p.name)
