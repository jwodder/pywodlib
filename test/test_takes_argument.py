from typing import Any, Callable
import pytest
from pywodlib.takes_argument import takes_argument


def simple(foo: Any) -> Any:
    return foo


def defaulting(foo: Any = None) -> Any:
    return foo


def kwarged(**kwargs: Any) -> dict:
    return kwargs


def arged(*foo: Any) -> tuple:
    return foo


# Python 3.8+:
# def pos_kwarg_only(foo: Any, /, bar: Any, *, baz: Any) -> Any:
#     return foo


@pytest.mark.parametrize(
    "func,arg,r",
    [
        (simple, "foo", True),
        (simple, "bar", False),
        (defaulting, "foo", True),
        (defaulting, "bar", False),
        (kwarged, "foo", True),
        (kwarged, "kwargs", True),
        (arged, "foo", False),
        # (pos_kwarg_only, "foo", False),
        # (pos_kwarg_only, "bar", True),
        # (pos_kwarg_only, "baz", True),
        # (pos_kwarg_only, "quux", False),
    ],
)
def test_takes_argument(func: Callable, argname: str, r: bool) -> None:
    assert takes_argument(func, argname) is r
