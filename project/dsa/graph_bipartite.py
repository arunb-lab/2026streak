"""Check if an undirected graph is bipartite.

Problem:
Given an undirected graph, determine if it can be colored using 2 colors such
that no adjacent nodes share the same color.

Input representation:
`graph[u]` is a list of neighbors of vertex `u` (0..n-1).

Approach:
BFS each connected component and 2-color it.

Time: O(V + E)
Space: O(V)
"""

from __future__ import annotations

from collections import deque


def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    color: list[int] = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        q: deque[int] = deque([start])
        color[start] = 0

        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False

    return True
