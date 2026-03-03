"""Hopcroft–Karp maximum bipartite matching.

Computes a maximum cardinality matching in a bipartite graph (U, V, E).

API:
- HopcroftKarp(n_left, n_right)
- add_edge(u, v)
- max_matching() -> int
- matching_left / matching_right arrays

Complexity:
- O(E * sqrt(V))

Refs:
- Hopcroft, Karp (1973)
"""

from __future__ import annotations

from collections import deque


class HopcroftKarp:
    def __init__(self, n_left: int, n_right: int) -> None:
        if n_left < 0 or n_right < 0:
            raise ValueError("side sizes must be non-negative")
        self.n_left = n_left
        self.n_right = n_right
        self.g: list[list[int]] = [[] for _ in range(n_left)]
        self.match_left: list[int] = [-1] * n_left
        self.match_right: list[int] = [-1] * n_right
        self._dist: list[int] = [0] * n_left

    def add_edge(self, u: int, v: int) -> None:
        if not (0 <= u < self.n_left and 0 <= v < self.n_right):
            raise IndexError("node out of range")
        self.g[u].append(v)

    def max_matching(self) -> int:
        """Return the size of a maximum matching."""

        matching = 0

        def bfs() -> bool:
            q: deque[int] = deque()
            for u in range(self.n_left):
                if self.match_left[u] == -1:
                    self._dist[u] = 0
                    q.append(u)
                else:
                    self._dist[u] = -1

            found_free = False
            while q:
                u = q.popleft()
                for v in self.g[u]:
                    u2 = self.match_right[v]
                    if u2 == -1:
                        found_free = True
                    elif self._dist[u2] == -1:
                        self._dist[u2] = self._dist[u] + 1
                        q.append(u2)
            return found_free

        def dfs(u: int) -> bool:
            for v in self.g[u]:
                u2 = self.match_right[v]
                if u2 == -1 or (self._dist[u2] == self._dist[u] + 1 and dfs(u2)):
                    self.match_left[u] = v
                    self.match_right[v] = u
                    return True
            self._dist[u] = -1
            return False

        while bfs():
            for u in range(self.n_left):
                if self.match_left[u] == -1:
                    if dfs(u):
                        matching += 1

        return matching
