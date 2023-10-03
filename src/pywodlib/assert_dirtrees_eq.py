from operator import attrgetter
from pathlib import Path


def assert_dirtrees_eq(tree1: Path, tree2: Path) -> None:
    """
    Assert that the directory hierarchies at ``tree1`` and ``tree2`` have the
    same files with the same contents.

    For use in writing pytest tests.
    """
    assert sorted(map(attrgetter("name"), tree1.iterdir())) == sorted(
        map(attrgetter("name"), tree2.iterdir())
    )
    for p1 in tree1.iterdir():
        p2 = tree2 / p1.name
        assert p1.is_dir() == p2.is_dir()
        if p1.is_dir():
            assert_dirtrees_eq(p1, p2)
        else:
            assert p1.read_text(encoding="utf-8") == p2.read_text(encoding="utf-8")
