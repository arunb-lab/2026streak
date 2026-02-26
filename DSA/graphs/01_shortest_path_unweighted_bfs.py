"""DSA - Graphs: Shortest Path in Unweighted Graph (BFS)

Problem:
Given an unweighted graph and a source node, compute shortest path distances
(number of edges) to every reachable node.

Approach:
Breadth-first search (BFS) from the source.

Time: O(V + E)
Space: O(V)
"""

from __future__ import annotations

from collections import deque


def shortest_path_unweighted_bfs(
    graph: dict[str, list[str]], source: str
) -> dict[str, int]:
    if source not in graph:
        raise ValueError("source must exist in graph")

    dist: dict[str, int] = {source: 0}
    q: deque[str] = deque([source])

    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)

    return dist


if __name__ == "__main__":
    g = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["E"],
        "E": [],
    }
    assert shortest_path_unweighted_bfs(g, "A") == {
        "A": 0,
        "B": 1,
        "C": 1,
        "D": 2,
        "E": 2,
    }
    print("ok")
