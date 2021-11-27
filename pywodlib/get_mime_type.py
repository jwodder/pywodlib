from mimetypes import guess_type
import pytest


def get_mime_type(filename, strict=False):
    # type: (str, bool) -> str
    """
    Like `mimetypes.guess_type()`, except that if the file is compressed, the
    MIME type for the compression is returned.  Also, the default return value
    is now ``'application/octet-stream'`` instead of `None`.
    """
    mtype, encoding = guess_type(filename, strict)
    if encoding is None:
        return mtype or "application/octet-stream"
    elif encoding == "gzip":
        # application/gzip is defined by RFC 6713
        return "application/gzip"
        # There is also a "+gzip" MIME structured syntax suffix defined by RFC
        # 8460; exactly when can that be used?
        # return mtype + '+gzip'
    else:
        return "application/x-" + encoding


@pytest.mark.parametrize(
    "filename,mtype",
    [
        ("foo.txt", "text/plain"),
        ("foo", "application/octet-stream"),
        ("foo.gz", "application/gzip"),
        ("foo.tar.gz", "application/gzip"),
        ("foo.tgz", "application/gzip"),
        ("foo.taz", "application/gzip"),
        ("foo.svg.gz", "application/gzip"),
        ("foo.svgz", "application/gzip"),
        ("foo.Z", "application/x-compress"),
        ("foo.tar.Z", "application/x-compress"),
        ("foo.bz2", "application/x-bzip2"),
        ("foo.tar.bz2", "application/x-bzip2"),
        ("foo.tbz2", "application/x-bzip2"),
        ("foo.xz", "application/x-xz"),
        ("foo.tar.xz", "application/x-xz"),
        ("foo.txz", "application/x-xz"),
    ],
)
def test_get_mime_type(filename, mtype):
    assert get_mime_type(filename) == mtype
