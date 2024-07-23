from pathlib import Path
import pytest
from pywodlib.under_path import under_path


@pytest.fixture(scope="module")
def faketree(tmp_path_factory: pytest.TempPathFactory) -> Path:
    base = tmp_path_factory.mktemp("under_path")
    (base / "foo" / "bar").mkdir(parents=True, exist_ok=True)
    (base / "gnusto" / "cleesh").mkdir(parents=True, exist_ok=True)
    (base / "gnusto" / "link").symlink_to(base / "foo")
    (base / "gnusto" / "link2").symlink_to(base)
    return base


@pytest.mark.parametrize(
    "p1,p2,r",
    [
        ("foo", "foo", True),
        ("foo/bar", "foo", True),
        ("foo", "foo/bar", False),
        ("gnusto", "foo", False),
        ("gnusto/..", "foo", False),
        ("gnusto", "foo/..", True),
        (".", "foo/..", True),
        ("foo", "foo/nexist", False),
        ("gnusto", "foo/nexist", False),
        ("foo", "nexist", False),
        ("gnusto/../foo/bar", "foo", True),
        ("foo", "gnusto/link", False),  # FAIL
        ("foo", "gnusto/link/bar", False),
        ("foo", "gnusto/link2", False),  # FAIL
        ("foo", "gnusto/link/..", True),
        ("foo", "gnusto", False),
        ("foo", "gnusto/../foo", True),
        ("gnusto/link/bar", "gnusto", True),  # FAIL
    ],
)
def test_under_path(
    faketree: Path, monkeypatch: pytest.MonkeyPatch, p1: str, p2: str, r: bool
) -> None:
    monkeypatch.chdir(faketree)
    assert under_path(p1, p2) is r
    assert under_path(faketree / p1, p2) is r
    assert under_path(p1, faketree / p2) is r
    assert under_path(faketree / p1, faketree / p2) is r
