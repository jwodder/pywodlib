def quantify(qty: int, singular: str, plural: str | None = None) -> str:
    # cf. the humanfriendly package's pluralize() function
    if qty == 1:
        return f"{qty} {singular}"
    elif plural is None:
        return f"{qty} {singular}s"
    else:
        return f"{qty} {plural}"
