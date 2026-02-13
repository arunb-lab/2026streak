"""Floyd–Warshall all-pairs shortest paths.

Works with:
- negative edge weights
- no negative cycles (if a negative cycle exists, distances can decrease forever)

Representation:
- nodes: any hashable labels (we use str in tests)
- edges: dict[u, list[(v, w)]] adjacency list

Returns:
- dist[u][v] = shortest distance from u to v (float('inf') if unreachable)

Time:  O(V^3)
Space: O(V^2)
"""

from __future__ import annotations

from math import inf
from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def floyd_warshall(graph: dict[T, list[tuple[T, float]]]) -> dict[T, dict[T, float]]:
    nodes: set[T] = set(graph.keys())
    for vs in graph.values():
        for v, _w in vs:
            nodes.add(v)

    dist: dict[T, dict[T, float]] = {u: {v: inf for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0.0

    for u, vs in graph.items():
        for v, w in vs:
            if w < dist[u][v]:
                dist[u][v] = float(w)

    # main DP: allow intermediate nodes in increasing set.
    for k in nodes:
        for i in nodes:
            dik = dist[i][k]
            if dik == inf:
                continue
            for j in nodes:
                alt = dik + dist[k][j]
                if alt < dist[i][j]:
                    dist[i][j] = alt

    return dist


def has_negative_cycle(dist: dict[T, dict[T, float]]) -> bool:
    """Detect negative cycle after Floyd–Warshall.

    A negative cycle exists iff dist[u][u] < 0 for some u.
    """

    return any(dist[u][u] < 0 for u in dist)
