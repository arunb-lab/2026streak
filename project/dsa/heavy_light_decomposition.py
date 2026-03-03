"""Heavy-Light Decomposition (HLD) for trees.

HLD decomposes tree paths into O(log n) segments on a base array.
This is typically paired with a segment tree / BIT on the base array.

This implementation provides:
- parent, depth
- head (top of heavy path)
- pos (position of node in base array)
- inv (node at position)
- decompose_path(u, v): yields segments [l, r] (inclusive) on base array
  that cover the path u-v.

Design choice:
- We yield segments in *any* order (from u and v climbing). If you need
  order-sensitive queries (e.g., path string concatenation), you'll need a
  variant that preserves direction.

Refs:
- Sleator & Tarjan (1983) style decomposition popularized in CP.
"""

from __future__ import annotations


class HeavyLightDecomposition:
    def __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        if not (0 <= root < n):
            raise IndexError("root out of range")

        g: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            if not (0 <= a < n and 0 <= b < n):
                raise IndexError("edge node out of range")
            g[a].append(b)
            g[b].append(a)

        self.n = n
        self.root = root
        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [0] * n
        self.heavy = [-1] * n

        # 1) parent/depth + order by stack.
        order: list[int] = []
        stack = [root]
        self.parent[root] = -1
        self.depth[root] = 0
        while stack:
            u = stack.pop()
            order.append(u)
            for v in g[u]:
                if v == self.parent[u]:
                    continue
                self.parent[v] = u
                self.depth[v] = self.depth[u] + 1
                stack.append(v)

        if len(order) != n:
            raise ValueError("graph is not connected (not a single tree)")

        # 2) subtree sizes + heavy child.
        for u in reversed(order):
            self.size[u] = 1
            best = (0, -1)
            for v in g[u]:
                if v == self.parent[u]:
                    continue
                self.size[u] += self.size[v]
                if self.size[v] > best[0]:
                    best = (self.size[v], v)
            self.heavy[u] = best[1]

        # 3) decompose.
        self.head = [0] * n
        self.pos = [0] * n
        self.inv = [0] * n

        cur_pos = 0
        stack2: list[tuple[int, int]] = [(root, root)]  # (start node, head)
        while stack2:
            u, h = stack2.pop()
            # Walk heavy path.
            x = u
            while x != -1:
                self.head[x] = h
                self.pos[x] = cur_pos
                self.inv[cur_pos] = x
                cur_pos += 1

                # Push light children as new paths.
                for v in g[x]:
                    if v == self.parent[x] or v == self.heavy[x]:
                        continue
                    stack2.append((v, v))

                x = self.heavy[x]

    def decompose_path(self, u: int, v: int) -> list[tuple[int, int]]:
        """Return list of base-array segments covering path u-v (inclusive)."""

        if not (0 <= u < self.n and 0 <= v < self.n):
            raise IndexError("node out of range")

        segs: list[tuple[int, int]] = []
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            hu = self.head[u]
            segs.append((self.pos[hu], self.pos[u]))
            u = self.parent[hu]
            if u == -1:
                break

        if u != -1 and v != -1:
            if self.depth[u] > self.depth[v]:
                u, v = v, u
            segs.append((self.pos[u], self.pos[v]))

        # normalize l<=r
        return [(l, r) if l <= r else (r, l) for (l, r) in segs]
