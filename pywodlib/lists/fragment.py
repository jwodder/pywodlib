def fragment(xs, n):
    if n < 1:
        raise ValueError("n must be at least 1")
    return [xs[i : i + n] for i in range(0, len(xs), n)]
