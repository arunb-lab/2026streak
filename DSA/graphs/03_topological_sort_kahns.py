"""DSA - Graphs: Topological Sort (Kahn's Algorithm)

Problem:
Given a directed graph, return a topological ordering of nodes if it exists.
If the graph contains a cycle, no topological order exists.

Approach:
- Compute indegree for each node.
- Initialize queue with nodes having indegree 0.
- Pop, append to order, decrement indegree of outgoing neighbors.

Time: O(V + E)
Space: O(V)
"""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable


def topo_sort(nodes: list[Hashable], edges: list[tuple[Hashable, Hashable]]) -> list[Hashable]:
    adj: dict[Hashable, list[Hashable]] = {n: [] for n in nodes}
    indeg: dict[Hashable, int] = {n: 0 for n in nodes}

    for u, v in edges:
        if u not in adj:
            adj[u] = []
            indeg[u] = 0
        if v not in adj:
            adj[v] = []
            indeg[v] = 0
        adj[u].append(v)
        indeg[v] += 1

    q = deque([n for n in adj if indeg[n] == 0])
    order: list[Hashable] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != len(adj):
        raise ValueError("graph has a cycle; topo order does not exist")

    return order


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    order = topo_sort(nodes, edges)
    pos = {n: i for i, n in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v]
    print("ok")
