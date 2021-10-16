def bytes2iso(numbytes):
    # cf. the humanize package's naturalsize() function
    """
    >>> bytes2iso(512)
    '512 B'
    >>> bytes2iso(1024)
    '1.00 kB'
    >>> bytes2iso(1000000)
    '976.56 kB'
    >>> bytes2iso(2334597576389)
    '2.12 TB'
    >>> bytes2iso(1152921504606846976000000)
    '1000000.00 EB'
    """
    size = numbytes
    sizestr = f"{size} B"
    for prefix in "kMGTPE":
        if size < 1024:
            return sizestr
        size /= 1024
        sizestr = f"{size:.2f} {prefix}B"
    return sizestr
