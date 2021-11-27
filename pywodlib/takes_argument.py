"""

>>> def simple(foo):
...     return foo
...
>>> takes_argument(simple, "foo")
True
>>> takes_argument(simple, "bar")
False

>>> def defaulting(foo=None):
...     return foo
...
>>> takes_argument(defaulting, "foo")
True
>>> takes_argument(defaulting, "bar")
False

>>> def kwarged(**kwargs):
...     return kwargs
...
>>> takes_argument(kwarged, "foo")
True
>>> takes_argument(kwarged, "kwargs")
True

>>> def arged(*foo):
...     return foo
...
>>> takes_argument(arged, "foo")
False

>>> def pos_kwarg_only(foo, /, bar, *, baz):
...     return foo
...
>>> takes_argument(pos_kwarg_only, "foo")
False
>>> takes_argument(pos_kwarg_only, "bar")
True
>>> takes_argument(pos_kwarg_only, "baz")
True
>>> takes_argument(pos_kwarg_only, "quux")
False

"""

import inspect
from typing import Any, Callable


def takes_argument(callable_obj: Callable[..., Any], argname: str) -> bool:
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
