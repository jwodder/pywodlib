import json


def qqrepr(s: str) -> str:
    """Produce a repr(string) enclosed in double quotes"""
    return json.dumps(s, ensure_ascii=False)
