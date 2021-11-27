import subprocess
import sys


def readcmd(*args, check=True, **kwargs):
    # TODO: Show a decent error message on failure
    r = subprocess.run(args, universal_newlines=True, stdout=subprocess.PIPE, **kwargs)
    if r.returncode == 0:
        return r.stdout.strip()
    elif check:
        sys.exit(r.returncode)
    else:
        return None
