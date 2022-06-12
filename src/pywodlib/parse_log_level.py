import logging


def parse_log_level(level: str) -> int:
    """
    Convert a log level name (case-insensitive) or number to its numeric value
    """
    try:
        return int(level)
    except ValueError:
        levelup = level.upper()
        if levelup in {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"}:
            ll = getattr(logging, levelup)
            assert isinstance(ll, int)
            return ll
        else:
            raise ValueError(f"Invalid log level: {level!r}")
