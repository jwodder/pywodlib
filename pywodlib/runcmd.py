#import shlex
import subprocess
from typing import Any, Union, cast

def runcmd(*args: Union[str, Path], **kwargs: Any) -> None:
    argstrs = [str(a) for a in args]
    #log.debug("Running: %s", " ".join(map(shlex.quote, argstrs)))
    r = subprocess.run(argstrs, **kwargs)
    if r.returncode != 0:
        sys.exit(r.returncode)

def readcmd(*args: Union[str, Path], **kwargs: Any) -> str:
    argstrs = [str(a) for a in args]
    #log.debug("Running: %s", " ".join(map(shlex.quote, argstrs)))
    try:
        return cast(str, subprocess.check_output(argstrs, universal_newlines=True, **kwargs)).strip()
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
