"""Bellman–Ford shortest paths.

Unlike Dijkstra, Bellman–Ford supports negative weights.
It can also detect reachable negative cycles.

Input:
- n nodes labeled 0..n-1
- directed edges (u, v, w)

Output:
- dist list with float('inf') for unreachable
- boolean flag indicating whether a negative cycle is reachable from source

Complexities:
- time:  O(VE)
- space: O(V)
"""

from __future__ import annotations


def bellman_ford(
    n: int, edges: list[tuple[int, int, int]], source: int
) -> tuple[list[float], bool]:
    if n <= 0:
        raise ValueError("n must be >= 1")
    if source < 0 or source >= n:
        raise IndexError("source out of range")

    dist: list[float] = [float("inf")] * n
    dist[source] = 0.0

    # Relax edges V-1 times.
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if u < 0 or u >= n or v < 0 or v >= n:
                raise IndexError("edge node out of range")
            if dist[u] == float("inf"):
                continue
            nd = dist[u] + float(w)
            if nd < dist[v]:
                dist[v] = nd
                changed = True
        if not changed:
            break

    # One more pass to detect negative cycle reachable from source.
    for u, v, w in edges:
        if dist[u] == float("inf"):
            continue
        if dist[u] + float(w) < dist[v]:
            return dist, True

    return dist, False
