from traceback import format_exception
from click.testing import Result


def show_result(r: Result) -> str:
    """
    If the test invocation that produced ``r`` raised an error, return the
    formatted traceback; otherwise, return the invocation's output
    """
    if r.exception is not None:
        assert isinstance(r.exc_info, tuple)
        return "".join(format_exception(*r.exc_info))
    else:
        return r.output
