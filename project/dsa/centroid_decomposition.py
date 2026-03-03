"""Centroid Decomposition of a tree.

Builds a centroid tree:
- centroid_parent[c] = parent centroid of c in the centroid decomposition (-1 for root)
- level[c] = depth in centroid tree

Useful for:
- Distance to nearest marked node
- Path queries with updates in O(log n)

This module only builds the decomposition; it does not implement a particular
query on top.

Complexity:
- O(n log n)
"""

from __future__ import annotations


class CentroidDecomposition:
    def __init__(self, n: int, edges: list[tuple[int, int]]) -> None:
        if n <= 0:
            raise ValueError("n must be positive")

        g: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            if not (0 <= a < n and 0 <= b < n):
                raise IndexError("edge node out of range")
            g[a].append(b)
            g[b].append(a)

        self.n = n
        self.g = g
        self.centroid_parent = [-1] * n
        self.level = [0] * n
        self._dead = [False] * n
        self._sub = [0] * n

        self._build(0, -1, 0)

    def _dfs_size(self, u: int, p: int) -> int:
        self._sub[u] = 1
        for v in self.g[u]:
            if v == p or self._dead[v]:
                continue
            self._sub[u] += self._dfs_size(v, u)
        return self._sub[u]

    def _dfs_centroid(self, u: int, p: int, total: int) -> int:
        for v in self.g[u]:
            if v == p or self._dead[v]:
                continue
            if self._sub[v] > total // 2:
                return self._dfs_centroid(v, u, total)
        return u

    def _build(self, entry: int, parent: int, lvl: int) -> None:
        total = self._dfs_size(entry, -1)
        c = self._dfs_centroid(entry, -1, total)
        self.centroid_parent[c] = parent
        self.level[c] = lvl
        self._dead[c] = True

        for v in self.g[c]:
            if self._dead[v]:
                continue
            self._build(v, c, lvl + 1)

        # Note: we intentionally keep _dead[c]=True so higher recursion levels
        # don't traverse through centroid again.
