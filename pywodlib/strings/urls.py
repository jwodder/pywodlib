def join_urls(base: str, path: str) -> str:
    if is_http_url(path):
        return path
    else:
        return base.rstrip("/") + "/" + path.lstrip("/")

def is_http_url(s: str) -> bool:
    return s.lower().startswith(("http://", "https://"))
