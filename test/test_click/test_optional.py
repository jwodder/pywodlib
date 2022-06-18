from __future__ import annotations
from typing import Any
from unittest.mock import Mock
import click
from click.testing import CliRunner
import pytest
from pywodlib.thirdparty.click.optional import optional
from pywodlib.thirdparty.click.show_result import show_result


@pytest.mark.parametrize(
    "cmdline,cmdkwargs",
    [
        ([], {}),
        (["--optional", "foo"], {"optional": "foo"}),
        (["--optional", ""], {"optional": ""}),
        (["--multi-optional=bar", "-M", "baz"], {"multi_optional": ("bar", "baz")}),
        (["-M", ""], {"multi_optional": ("",)}),
        (["--nilstr="], {"nilstr": None}),
        (["--multi-nilstr", ""], {"multi_nilstr": ()}),
        (["--multi-nilstr", "", "-Nfoo"], {"multi_nilstr": ("", "foo")}),
        (["--multi-nilstr", "foo", "-N", ""], {"multi_nilstr": ("foo", "")}),
    ],
)
def test_optional(cmdline: list[str], cmdkwargs: dict[str, Any]) -> None:
    mock = Mock()

    @click.command()
    @optional("--optional")
    @optional("-M", "--multi-optional", multiple=True)
    @optional("--nilstr", nilstr=True)
    @optional("-N", "--multi-nilstr", multiple=True, nilstr=True)
    def cmd(**kwargs: Any) -> None:
        mock(**kwargs)

    r = CliRunner().invoke(cmd, cmdline, standalone_mode=False)
    assert r.exit_code == 0, show_result(r)
    mock.assert_called_once_with(**cmdkwargs)
