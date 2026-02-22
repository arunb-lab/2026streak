"""Dinic's max flow algorithm.

Computes maximum flow in a directed graph with non-negative capacities.

Implementation details:
- Uses adjacency lists of edges with reverse indices (classic competitive
  programming style).
- Complexity: O(E * V^2) worst-case, often much faster in practice.

Refs:
- Dinic, 1970.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class _Edge:
    to: int
    rev: int
    cap: float


class Dinic:
    def __init__(self, n: int) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        self.n = n
        self.g: list[list[_Edge]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: float) -> None:
        """Add directed edge u->v with given capacity."""

        if cap < 0:
            raise ValueError("capacity must be non-negative")
        if not (0 <= u < self.n and 0 <= v < self.n):
            raise IndexError("node out of range")

        fwd = _Edge(to=v, rev=len(self.g[v]), cap=float(cap))
        rev = _Edge(to=u, rev=len(self.g[u]), cap=0.0)
        self.g[u].append(fwd)
        self.g[v].append(rev)

    def max_flow(self, s: int, t: int) -> float:
        if not (0 <= s < self.n and 0 <= t < self.n):
            raise IndexError("node out of range")
        if s == t:
            return 0.0

        flow = 0.0
        level: list[int] = [-1] * self.n
        it: list[int] = [0] * self.n

        def bfs() -> bool:
            for i in range(self.n):
                level[i] = -1
            level[s] = 0
            q: deque[int] = deque([s])
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e.cap > 0 and level[e.to] < 0:
                        level[e.to] = level[u] + 1
                        q.append(e.to)
            return level[t] >= 0

        def dfs(u: int, f: float) -> float:
            if u == t:
                return f
            for i in range(it[u], len(self.g[u])):
                it[u] = i
                e = self.g[u][i]
                if e.cap <= 0:
                    continue
                if level[e.to] != level[u] + 1:
                    continue
                pushed = dfs(e.to, min(f, e.cap))
                if pushed > 0:
                    e.cap -= pushed
                    self.g[e.to][e.rev].cap += pushed
                    return pushed
            return 0.0

        while bfs():
            it = [0] * self.n
            while True:
                pushed = dfs(s, float("inf"))
                if pushed == 0:
                    break
                flow += pushed

        return flow


def max_flow(n: int, edges: list[tuple[int, int, float]], s: int, t: int) -> float:
    """Convenience wrapper to compute max flow."""

    d = Dinic(n)
    for u, v, c in edges:
        d.add_edge(u, v, c)
    return d.max_flow(s, t)
