"""DSA - Graphs: Dijkstra's Shortest Path (non-negative weights)

Problem:
Given a directed/undirected weighted graph with non-negative edge weights,
compute the shortest distance from a start node to all nodes.

Graph representation:
adj[u] = list of (v, w) edges.

Algorithm:
- Use a min-heap keyed by current known distance.
- When a node is popped with a stale (larger) distance, skip it.

Time: O((V+E) log V)
Space: O(V)
"""

from __future__ import annotations

import heapq
from collections.abc import Hashable


def dijkstra(adj: dict[Hashable, list[tuple[Hashable, int]]], start: Hashable) -> dict[Hashable, int]:
    dist: dict[Hashable, int] = {start: 0}
    pq: list[tuple[int, Hashable]] = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist.get(u, None):
            continue

        for v, w in adj.get(u, []):
            if w < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            nd = d + w
            if nd < dist.get(v, 10**30):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist


if __name__ == "__main__":
    g = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    assert dijkstra(g, "A") == {"A": 0, "B": 1, "C": 3, "D": 4}
    print("ok")
