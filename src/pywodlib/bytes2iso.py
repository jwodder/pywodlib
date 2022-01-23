from typing import Union


def bytes2iso(numbytes: int) -> str:
    # cf. the humanize package's naturalsize() function
    size: Union[int, float] = numbytes
    sizestr = f"{size} B"
    for prefix in "kMGTPEZY":
        if size < 1024:
            return sizestr
        size /= 1024
        sizestr = f"{size:.2f} {prefix}B"
    return sizestr
