"""0-1 BFS for shortest paths with edge weights in {0, 1}.

For graphs where each edge weight is 0 or 1, Dijkstra can be optimized to O(V+E)
by using a deque:
- When relaxing a 0-weight edge, pushleft.
- When relaxing a 1-weight edge, pushright.

This yields the same result as Dijkstra but faster and simpler.

Time complexity: O(V + E)
Space complexity: O(V)
"""

from __future__ import annotations

from collections import deque
from math import inf


def bfs_01(
    n: int, edges: list[tuple[int, int, int]], source: int
) -> list[float]:
    """Compute shortest path distances from ``source`` in a 0/1 weighted digraph.

    Args:
        n: Number of nodes labeled [0..n-1].
        edges: List of directed edges (u, v, w) where w is 0 or 1.
        source: Source node.

    Returns:
        dist array where dist[v] is min cost from source to v (inf if unreachable).

    Raises:
        ValueError: If n <= 0 or any weight is not 0/1.
        IndexError: If a node index is out of bounds.
    """

    if n <= 0:
        raise ValueError("n must be positive")
    if source < 0 or source >= n:
        raise IndexError("source out of range")

    g: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        if not (0 <= u < n and 0 <= v < n):
            raise IndexError("edge endpoint out of range")
        if w not in (0, 1):
            raise ValueError("0-1 BFS requires weights in {0,1}")
        g[u].append((v, w))

    dist: list[float] = [inf] * n
    dist[source] = 0.0

    dq: deque[int] = deque([source])

    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in g[u]:
            nd = du + float(w)
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist
