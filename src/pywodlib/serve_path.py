from __future__ import annotations
from collections.abc import Iterator
from contextlib import contextmanager
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread


@contextmanager
def serve_path(dirpath: str | Path, bind_address: str = "127.0.0.1") -> Iterator[str]:
    """
    Returns a context manager that serves the contents of the directory
    ``dirpath`` over HTTP at ``bind_address`` and a random port.  On entry, the
    context manager returns the URL at which the directory is being served.
    """
    with HTTPServer(
        (bind_address, 0), partial(SimpleHTTPRequestHandler, directory=dirpath)
    ) as httpd:
        t = Thread(target=httpd.serve_forever)
        t.start()
        try:
            server_name, *_ = httpd.server_address
            # `httpd.server_name` is run through `socket.getfqdn()`, which (on
            # Python 3.9 on macOS, at least) converts IP addresses to .arpa
            # addresses, which don't work with requests, so we can't use that.
            if ":" in server_name:
                yield f"http://[{server_name}]:{httpd.server_port}"
            else:
                yield f"http://{server_name}:{httpd.server_port}"
        finally:
            httpd.shutdown()
            t.join()
