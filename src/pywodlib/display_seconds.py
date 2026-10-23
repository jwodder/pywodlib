def display_seconds(seconds: int) -> str:
    dhm, seconds = divmod(seconds, 60)
    dh, minutes = divmod(dhm, 60)
    days, hours = divmod(dh, 24)
    bits = []
    for qty, unit in [
        (days, "day"),
        (hours, "hour"),
        (minutes, "minute"),
        (seconds, "seconds"),
    ]:
        if qty:
            s = f"{qty} {unit}"
            if qty > 1:
                s += "s"
            bits.append(s)
    if bits:
        return ", ".join(bits)
    else:
        return "---"
