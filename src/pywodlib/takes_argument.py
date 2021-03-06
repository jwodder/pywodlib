from __future__ import annotations
from collections.abc import Callable
import inspect


def takes_argument(callable_obj: Callable, argname: str) -> bool:
    """
    Returns true iff ``callable_obj`` can be passed an argument named
    ``argname`` by keyword
    """
    sig = inspect.signature(callable_obj)
    for param in sig.parameters.values():
        if (
            param.kind in (param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY)
            and param.name == argname
        ):
            return True
        elif param.kind is param.VAR_KEYWORD:
            return True
    return False
