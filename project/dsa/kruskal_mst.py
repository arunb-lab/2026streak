"""Kruskal's algorithm for Minimum Spanning Tree (MST).

For an undirected, connected graph with weighted edges, an MST has:
- V-1 edges
- minimum total weight

If the graph is disconnected, Kruskal produces a minimum spanning forest.

Input:
- edges: list[(u, v, w)] where u and v are hashable node labels

Output:
- (total_weight, mst_edges)

Time:  O(E log E)
Space: O(V)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass
class _DSU:
    parent: dict[T, T]
    rank: dict[T, int]

    @classmethod
    def from_nodes(cls, nodes: set[T]) -> "_DSU[T]":
        return cls(parent={n: n for n in nodes}, rank={n: 0 for n in nodes})

    def find(self, x: T) -> T:
        p = self.parent[x]
        if p != x:
            self.parent[x] = self.find(p)
        return self.parent[x]

    def union(self, a: T, b: T) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def kruskal_mst(edges: list[tuple[T, T, float]]) -> tuple[float, list[tuple[T, T, float]]]:
    nodes: set[T] = set()
    for u, v, _w in edges:
        nodes.add(u)
        nodes.add(v)

    dsu = _DSU.from_nodes(nodes)

    total = 0.0
    out: list[tuple[T, T, float]] = []

    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            out.append((u, v, float(w)))
            total += float(w)

    return total, out
