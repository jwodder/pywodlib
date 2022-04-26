### Make this a package and promote on
### <https://stackoverflow.com/q/41074796/744178>?
### TODO: Add `cache=True` (or `sys_modules=True`?) arguments to the functions
### to control whether `sys.modules` is used

### cf. <https://github.com/pytest-dev/pytest/blob/3c45175/src/_pytest/pathlib.py#L492-L508>

import importlib
import pkgutil
import sys
from types import ModuleType
from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Union,
    cast,
)


class ModuleData(NamedTuple):  ### TODO: Come up with a better name
    module: ModuleType
    absolute_name: str
    name: str  ### "relative_name"?  "child_name"?  "module_name"?
    is_pkg: bool


def iter_package(
    package: Union[str, ModuleType],
    path: Optional[List[str]] = None,  ### Should this be "private"?
    onerror: Optional[Callable[[str], Any]] = None,
) -> Iterator[ModuleData]:
    if isinstance(package, str):
        ### Load package from `path` if given?
        pkgname = package
        pkg = importlib.import_module(package)
    else:
        pkgname = package.__package__
        pkg = package
    if path is None:
        path = cast(Iterable[str], getattr(pkg, "__path__", None) or [])
    for m in pkgutil.iter_modules(list(path), prefix=f"{pkgname}."):
        try:
            module = import_module_info(m)
        except ImportError:
            if onerror is not None:
                onerror(m.name)
        except Exception:
            if onerror is not None:
                onerror(m.name)
            else:
                raise
        else:
            _, _, name = m.name.rpartition(".")
            setattr(pkg, name, module)
            yield ModuleData(module, m.name, name, m.ispkg)


def walk_package(
    package: Union[str, ModuleType],
    path: Optional[List[str]] = None,  ### Should this be "private"?
    onerror: Optional[Callable[[str], Any]] = None,
) -> Iterator[ModuleData]:
    seen = set()
    for data in iter_package(package, path, onerror):
        yield data
        if data.is_pkg:
            path = getattr(data.module, "__path__", None) or []
            # Don't traverse path items we've seen before
            newpath = []
            for p in path:
                if p not in seen:
                    newpath.append(p)
                    seen.add(p)
            ### TODO: Should .name be adjusted to be relative to the original
            ### package name?
            yield from walk_package(data.module, newpath, onerror)


def import_module_info(m: pkgutil.ModuleInfo, prefix=""):
    ### Should this take a `package` object on which to assign the loaded
    ### module?
    # cf. <https://docs.python.org/3/library/importlib.html#approximating
    #      -importlib-import-module>
    name = f"{prefix}{m.name}"
    if name in sys.modules:
        return sys.modules[name]
    spec = m.module_finder.find_spec(name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def import_module_at_path(module_name, file_path):
    ### Packages have to be loaded by pointing file_path to the __init__.py
    ### (How does this work for namespace packages?)
    ### TODO: Check sys.modules?
    ### cf. <https://stackoverflow.com/a/37124336/744178>
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


### TODO: Add an "import_module_under_path(module_name, dirpath)" function that
### imports the given module whose package root is in dirpath
