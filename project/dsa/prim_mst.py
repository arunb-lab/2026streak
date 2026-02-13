"""Prim's algorithm for Minimum Spanning Tree (MST).

Prim grows an MST from a start node by repeatedly adding the cheapest edge
crossing the cut (visited vs unvisited).

Input:
- graph: adjacency list {u: [(v, w), ...]} for an *undirected* graph.
  (You can provide each undirected edge twice: u->v and v->u.)

Output:
- (total_weight, mst_edges)

Raises:
- ValueError if the graph is disconnected (can't form a spanning tree).

Time:  O(E log V) using a heap.
Space: O(V)
"""

from __future__ import annotations

import heapq
from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def prim_mst(
    graph: dict[T, list[tuple[T, float]]], *, start: T | None = None
) -> tuple[float, list[tuple[T, T, float]]]:
    nodes: set[T] = set(graph.keys())
    for vs in graph.values():
        for v, _w in vs:
            nodes.add(v)

    if not nodes:
        return 0.0, []

    if start is None:
        start = next(iter(nodes))

    visited: set[T] = {start}
    heap: list[tuple[float, T, T]] = []  # (w, u, v)

    for v, w in graph.get(start, []):
        heapq.heappush(heap, (float(w), start, v))

    total = 0.0
    out: list[tuple[T, T, float]] = []

    while heap and len(visited) < len(nodes):
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        out.append((u, v, w))
        total += w
        for nv, nw in graph.get(v, []):
            if nv not in visited:
                heapq.heappush(heap, (float(nw), v, nv))

    if len(visited) != len(nodes):
        raise ValueError("graph is disconnected")

    return total, out
