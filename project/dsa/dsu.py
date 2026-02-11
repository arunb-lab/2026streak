"""Disjoint Set Union (Union-Find).

Supports:
- union(a, b)
- find(x) with path compression
- union by size

Typical uses:
- connected components
- Kruskal's MST
- dynamic connectivity
"""

from __future__ import annotations


class DSU:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be >= 0")
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find representative/root of x."""

        if x < 0 or x >= len(self.parent):
            raise IndexError("x out of range")

        # Path compression.
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != x:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, a: int, b: int) -> bool:
        """Union sets. Returns True if merged, False if already same set."""

        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        # Union by size.
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    """Count connected components in an undirected graph with nodes 0..n-1."""

    dsu = DSU(n)
    for a, b in edges:
        dsu.union(a, b)
    return dsu.components
