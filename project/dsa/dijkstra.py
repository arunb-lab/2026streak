"""Dijkstra's algorithm (single-source shortest paths, non-negative weights).

Graph representation:
    graph[u] = list of (v, weight)

Returns distances + an optional reconstructed path.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass


@dataclass(frozen=True)
class DijkstraResult:
    dist: dict[str, float]
    parent: dict[str, str | None]

    def path_to(self, target: str) -> list[str] | None:
        if target not in self.parent:
            return None
        path: list[str] = []
        cur: str | None = target
        while cur is not None:
            path.append(cur)
            cur = self.parent[cur]
        path.reverse()
        return path


def dijkstra(graph: dict[str, list[tuple[str, float]]], start: str) -> DijkstraResult:
    """Compute shortest distances from `start`.

    Raises:
        ValueError: if a negative edge weight is found.

    Time:  O((V+E) log V)
    Space: O(V)
    """

    for u, edges in graph.items():
        for v, w in edges:
            if w < 0:
                raise ValueError(f"negative weight edge: {u}->{v} = {w}")

    dist: dict[str, float] = {start: 0.0}
    parent: dict[str, str | None] = {start: None}
    pq: list[tuple[float, str]] = [(0.0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist.get(u, float("inf")):
            continue

        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    return DijkstraResult(dist=dist, parent=parent)
