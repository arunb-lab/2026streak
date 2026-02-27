"""Detect cycle in a directed graph.

Problem:
Given a directed graph, determine whether it contains a cycle.

Input representation:
`graph[u]` is a list of outgoing neighbors from vertex `u` (0..n-1).

Approach:
DFS with 3-color marking:
- 0 = unvisited
- 1 = visiting (in recursion stack)
- 2 = done
A back-edge to a `visiting` node indicates a cycle.

Time: O(V + E)
Space: O(V)
"""

from __future__ import annotations


def has_cycle_directed(graph: list[list[int]]) -> bool:
    n = len(graph)
    state: list[int] = [0] * n

    def dfs(u: int) -> bool:
        state[u] = 1
        for v in graph[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    for i in range(n):
        if state[i] == 0 and dfs(i):
            return True

    return False
