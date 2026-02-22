"""Tarjan's algorithm for strongly connected components (SCC).

Given a directed graph as an adjacency list, this module computes SCCs in
O(V+E) time.

Conventions:
- Graph keys can be any hashable type, but we assume `str` in type hints for
  readability.
- Nodes that appear only in adjacency lists are still treated as nodes.

Refs:
- Robert Tarjan, 1972.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TarjanResult:
    """Result for SCC computation."""

    components: list[list[str]]
    component_id: dict[str, int]


def _all_nodes(graph: dict[str, list[str]]) -> set[str]:
    nodes: set[str] = set(graph.keys())
    for vs in graph.values():
        nodes.update(vs)
    return nodes


def tarjan_scc(graph: dict[str, list[str]]) -> TarjanResult:
    """Compute SCCs using Tarjan's algorithm.

    Args:
        graph: adjacency list of a directed graph.

    Returns:
        TarjanResult with components in the order they are found.

    Notes:
        - The components are *not* guaranteed to be topologically sorted.
        - Isolated nodes appear as singleton SCCs.
    """

    nodes = _all_nodes(graph)

    index: int = 0
    index_of: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []

    comps: list[list[str]] = []
    comp_id: dict[str, int] = {}

    def push(v: str) -> None:
        nonlocal index
        index_of[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

    def pop_component(root: str) -> list[str]:
        comp: list[str] = []
        while True:
            w = stack.pop()
            on_stack.remove(w)
            comp.append(w)
            if w == root:
                break
        return comp

    def dfs(v: str) -> None:
        push(v)

        for w in graph.get(v, []):
            if w not in index_of:
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], index_of[w])

        # If v is a root node, pop the stack and generate an SCC.
        if lowlink[v] == index_of[v]:
            comp = pop_component(v)
            cid = len(comps)
            for x in comp:
                comp_id[x] = cid
            comps.append(comp)

    for v in sorted(nodes):
        if v not in index_of:
            dfs(v)

    return TarjanResult(components=comps, component_id=comp_id)


def condensation_dag(graph: dict[str, list[str]], scc: TarjanResult) -> dict[int, set[int]]:
    """Build the condensation DAG of SCCs.

    Returns:
        A DAG where each SCC is a node (by component id) and edges are between
        different SCCs.
    """

    dag: dict[int, set[int]] = {i: set() for i in range(len(scc.components))}
    for u, vs in graph.items():
        cu = scc.component_id[u]
        for v in vs:
            cv = scc.component_id[v]
            if cu != cv:
                dag[cu].add(cv)
    return dag


def topo_sort_dag(dag: dict[int, Iterable[int]]) -> list[int]:
    """Topologically sort a DAG (Kahn's algorithm)."""

    indeg: dict[int, int] = {u: 0 for u in dag}
    for u, vs in dag.items():
        for v in vs:
            indeg[v] = indeg.get(v, 0) + 1
            if v not in dag:
                dag = {**dag, v: []}  # ensure keys exist

    q: list[int] = sorted([u for u, d in indeg.items() if d == 0])
    out: list[int] = []

    # q is small; keep it sorted for determinism.
    while q:
        u = q.pop(0)
        out.append(u)
        for v in dag.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
                q.sort()

    if len(out) != len(indeg):
        raise ValueError("graph is not a DAG")

    return out
