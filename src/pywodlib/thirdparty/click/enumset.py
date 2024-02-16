from __future__ import annotations
from enum import Enum
import re
from typing import Generic, TypeVar
import click

E = TypeVar("E", bound=Enum)


class EnumSet(click.ParamType, Generic[E]):
    """
    ``EnumSet(klass)``, where ``klass`` is an `Enum` class whose values are
    strings, produces a `click` parameter type that parses comma-separated enum
    values into sets of `Enum` members.
    """

    name = "enumset"

    def __init__(self, klass: type[E]) -> None:
        self.klass = klass

    def convert(
        self,
        value: str | set[E],
        param: click.Parameter | None,
        ctx: click.Context | None,
    ) -> set[E]:
        if not isinstance(value, str):
            return value
        selected = set()
        for v in re.split(r"\s*,\s*", value):
            try:
                selected.add(self.klass(v))
            except ValueError:
                self.fail(f"{value!r}: invalid item {v!r}", param, ctx)
        return selected

    def get_metavar(self, _param: click.Parameter) -> str:
        return "[" + ",".join(v.value for v in self.klass) + "]"
