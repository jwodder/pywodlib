from __future__ import annotations
from collections.abc import Callable
from math import inf


def diameter(n_vertices: int, adjacent: Callable[[int], list[int]]) -> int:
    """
    Given an undirected, unweighted graph composed of ``n_vertices`` vertices,
    each identified by an integer in ``range(n_vertices)``, and a function
    ``adjacent`` that maps each vertex to a list of adjacent vertices, this
    function returns the diameter of the graph, i.e., the maximum distance
    between distinct vertices.

    >>> diameter(*from_matrix([
    ...     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ...     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ...     [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    ...     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ...     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ...     [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    ...     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    ...     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    ...     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    ...     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    ...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    ...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    ...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    ... ]))
    4
    >>> diameter(*from_matrix([
    ...     [0, 1, 1],
    ...     [1, 0, 1],
    ...     [1, 1, 0],
    ... ]))
    1
    >>> diameter(*from_matrix([
    ...     [0, 0, 1, 1, 1],
    ...     [0, 0, 1, 1, 1],
    ...     [1, 1, 0, 0, 0],
    ...     [1, 1, 0, 0, 0],
    ...     [1, 1, 0, 0, 0],
    ... ]))
    2
    """

    dists = [[inf] * n_vertices for _ in range(n_vertices)]
    for i in range(n_vertices):
        dists[i][i] = 0
        for j in adjacent(i):
            if j < i:
                dists[i][j] = dists[j][i] = 1
                # Connect j and everything that connects to it to i and
                # everything that connects to it:
                for k in range(i + 1):
                    for m in range(i + 1):
                        # If k connects to j and m connects to i, connect k to m
                        dists[k][m] = dists[m][k] = min(
                            dists[k][m], dists[k][j] + 1 + dists[i][m]
                        )
    diam = max(d for row in dists for d in row)
    assert isinstance(diam, int)
    return diam


def from_matrix(mat: list[list[int]]) -> tuple[int, Callable[[int], list[int]]]:
    return (len(mat), lambda i: [j for j, a in enumerate(mat[i]) if a])
