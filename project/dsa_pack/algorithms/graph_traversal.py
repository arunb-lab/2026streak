from __future__ import annotations

from collections import deque
from typing import Deque, Dict, Iterable, List, Set, Tuple

Graph = Dict[str, List[str]]


def build_undirected_graph(edges: Iterable[Tuple[str, str]]) -> Graph:
    graph: Graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    return graph


def bfs_order(graph: Graph, start: str) -> List[str]:
    """Return nodes visited in BFS order (deterministic for given adjacency lists)."""

    if start not in graph:
        return [start]

    q: Deque[str] = deque([start])
    seen: Set[str] = {start}
    out: List[str] = []

    while q:
        node = q.popleft()
        out.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)

    return out


def dfs_order(graph: Graph, start: str) -> List[str]:
    """Return nodes visited in DFS (recursive) preorder."""

    out: List[str] = []
    seen: Set[str] = set()

    def visit(node: str) -> None:
        seen.add(node)
        out.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                visit(nxt)

    if start not in graph:
        return [start]

    visit(start)
    return out
