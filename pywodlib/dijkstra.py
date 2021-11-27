def dijkstra_length(start, end, neighbors, length):
    """
    Returns the length of the shortest path from ``start`` to ``end``.
    ``neighbors`` must be a function that takes a vertex and returns an
    iterable of all of its neighbors.  ``length`` must be a function that takes
    two neighboring vertices ``x`` and ``y`` and returns the length of the edge
    from ``x`` to ``y``.  All vertices must be hashable.
    """
    visited = set()
    distances = {start: 0}
    current = start
    while True:
        for p in neighbors(current):
            if p not in visited:
                newdist = distances[current] + length(current, p)
                olddist = distances.get(p, None)
                if olddist is None or olddist > newdist:
                    distances[p] = newdist
        visited.add(current)
        if end in visited:
            return distances[end]
        visitable = [p for p in distances if p not in visited]
        if visitable:
            current = min(visitable, key=distances.__getitem__)
        else:
            raise ValueError("No route to endpoint")
