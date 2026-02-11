"""Graph traversal (BFS/DFS) examples.

Represent the graph as an adjacency list: dict[node, list[node]].

Includes:
- BFS shortest path in an unweighted graph
- DFS-based topological sort (DAG)
"""

from __future__ import annotations

from collections import deque


def bfs_shortest_path(
    graph: dict[str, list[str]], start: str, goal: str
) -> list[str] | None:
    """Shortest path from start to goal in an unweighted graph.

    Returns list of nodes from start..goal, or None if unreachable.

    Time:  O(V+E)
    Space: O(V)
    """

    if start == goal:
        return [start]

    q: deque[str] = deque([start])
    parent: dict[str, str | None] = {start: None}

    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v in parent:
                continue
            parent[v] = u
            if v == goal:
                # Reconstruct.
                path = [goal]
                cur = u
                while cur is not None:
                    path.append(cur)
                    cur = parent[cur]
                path.reverse()
                return path
            q.append(v)

    return None


def topo_sort_dfs(graph: dict[str, list[str]]) -> list[str]:
    """Topological sort of a DAG.

    Raises:
        ValueError: if a cycle is detected.

    Time:  O(V+E)
    Space: O(V)
    """

    order: list[str] = []
    state: dict[str, int] = {}  # 0=unseen, 1=visiting, 2=done

    def dfs(u: str) -> None:
        st = state.get(u, 0)
        if st == 1:
            raise ValueError("cycle detected")
        if st == 2:
            return
        state[u] = 1
        for v in graph.get(u, []):
            dfs(v)
        state[u] = 2
        order.append(u)

    # Ensure we visit isolated nodes that appear only as neighbors.
    nodes: set[str] = set(graph.keys())
    for vs in graph.values():
        nodes.update(vs)

    for n in sorted(nodes):
        if state.get(n, 0) == 0:
            dfs(n)

    order.reverse()
    return order
