from pathlib import Path


def rm_to_root(filepath: Path, rootdir: Path) -> None:
    """
    Unlink the file ``filepath`` and all parent directories recursively, as
    long as each such directory is empty (after deleting the previous node) and
    not equal to ``rootdir``
    """
    filepath.unlink()
    d = filepath.parent
    while d != rootdir and not any(d.iterdir()):
        d.rmdir()
        d = d.parent
