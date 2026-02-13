"""Strongly Connected Components (SCC) via Kosaraju's algorithm.

Kosaraju:
1) DFS on original graph to compute finishing order
2) DFS on transposed graph in reverse finishing order

Input:
- graph: adjacency list (directed) {u: [v, ...]}

Output:
- list of SCCs, each SCC is a list of nodes
  (SCC order is deterministic by sorting nodes during traversal)

Time:  O(V+E)
Space: O(V+E)
"""

from __future__ import annotations

from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def kosaraju_scc(graph: dict[T, list[T]]) -> list[list[T]]:
    nodes: set[T] = set(graph.keys())
    for vs in graph.values():
        nodes.update(vs)

    def build_rev() -> dict[T, list[T]]:
        rev: dict[T, list[T]] = {n: [] for n in nodes}
        for u, vs in graph.items():
            for v in vs:
                rev[v].append(u)
        for n in rev:
            rev[n].sort()
        return rev

    rev = build_rev()

    seen: set[T] = set()
    order: list[T] = []

    def dfs1(u: T) -> None:
        seen.add(u)
        for v in sorted(graph.get(u, [])):
            if v not in seen:
                dfs1(v)
        order.append(u)

    for n in sorted(nodes):
        if n not in seen:
            dfs1(n)

    seen.clear()
    out: list[list[T]] = []

    def dfs2(u: T, comp: list[T]) -> None:
        seen.add(u)
        comp.append(u)
        for v in rev.get(u, []):
            if v not in seen:
                dfs2(v, comp)

    for n in reversed(order):
        if n not in seen:
            comp: list[T] = []
            dfs2(n, comp)
            out.append(comp)

    return out
