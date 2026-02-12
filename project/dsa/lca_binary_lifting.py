"""Lowest Common Ancestor (LCA) via binary lifting.

Given a rooted tree, preprocess parent pointers in powers of two.
Then LCA queries run in O(log n).

Provides:
- kth_ancestor(u, k)
- lca(u, v)

Nodes are assumed to be integers 0..n-1.
"""

from __future__ import annotations

from collections import deque


class LCA:
    def __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0):
        if n < 0:
            raise ValueError("n must be >= 0")
        if n == 0:
            raise ValueError("n must be >= 1")
        if root < 0 or root >= n:
            raise IndexError("root out of range")

        g: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            if a < 0 or a >= n or b < 0 or b >= n:
                raise IndexError("edge node out of range")
            g[a].append(b)
            g[b].append(a)

        self._n = n
        self._root = root
        self._log = n.bit_length()
        self._up = [[-1] * n for _ in range(self._log)]
        self._depth = [-1] * n

        # BFS to compute parent and depth.
        q: deque[int] = deque([root])
        self._depth[root] = 0
        self._up[0][root] = -1

        while q:
            u = q.popleft()
            for v in g[u]:
                if self._depth[v] != -1:
                    continue
                self._depth[v] = self._depth[u] + 1
                self._up[0][v] = u
                q.append(v)

        if any(d == -1 for d in self._depth):
            raise ValueError("graph is not connected (not a single tree)")

        # Build binary lifting table.
        for j in range(1, self._log):
            for v in range(n):
                p = self._up[j - 1][v]
                self._up[j][v] = -1 if p == -1 else self._up[j - 1][p]

    @property
    def depth(self) -> list[int]:
        return self._depth[:]

    def kth_ancestor(self, u: int, k: int) -> int:
        if u < 0 or u >= self._n:
            raise IndexError("u out of range")
        if k < 0:
            raise ValueError("k must be >= 0")

        cur = u
        j = 0
        while k and cur != -1:
            if k & 1:
                cur = self._up[j][cur]
            k >>= 1
            j += 1
        return cur

    def lca(self, a: int, b: int) -> int:
        if a < 0 or a >= self._n or b < 0 or b >= self._n:
            raise IndexError("node out of range")

        if self._depth[a] < self._depth[b]:
            a, b = b, a

        # Lift a up to b's depth.
        diff = self._depth[a] - self._depth[b]
        a = self.kth_ancestor(a, diff)
        if a == b:
            return a

        for j in range(self._log - 1, -1, -1):
            if self._up[j][a] != self._up[j][b]:
                a = self._up[j][a]
                b = self._up[j][b]

        # Now parents match.
        return self._up[0][a]
