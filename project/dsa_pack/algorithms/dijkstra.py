from __future__ import annotations

import heapq
from typing import Dict, Iterable, List, Optional, Tuple

WeightedGraph = Dict[str, List[Tuple[str, int]]]


def build_directed_weighted(edges: Iterable[Tuple[str, str, int]]) -> WeightedGraph:
    g: WeightedGraph = {}
    for a, b, w in edges:
        g.setdefault(a, []).append((b, w))
        g.setdefault(b, [])
    return g


def dijkstra_shortest_paths(graph: WeightedGraph, start: str) -> Dict[str, int]:
    """Compute shortest distances from start using Dijkstra (non-negative weights)."""

    dist: Dict[str, int] = {start: 0}
    pq: List[Tuple[int, str]] = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d != dist.get(node):
            continue

        for nxt, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nxt, 10**18):
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist


def shortest_path_to(graph: WeightedGraph, start: str, goal: str) -> Optional[int]:
    """Convenience wrapper: returns distance to goal or None if unreachable."""

    dist = dijkstra_shortest_paths(graph, start)
    return dist.get(goal)
