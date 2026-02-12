"""Topological sorting (Kahn's algorithm).

Kahn's algorithm uses in-degrees and a queue:
- repeatedly pick nodes with in-degree 0
- remove their outgoing edges (decrement in-degrees)

It is useful when you want:
- an iterative topo sort
- easy cycle detection (if processed_count < V)

This implementation optionally produces a deterministic order by sorting the
zero in-degree queue.
"""

from __future__ import annotations

from collections import deque
from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def kahn_topo_sort(
    graph: dict[T, list[T]], *, deterministic: bool = True
) -> list[T]:
    """Return a topological ordering.

    Args:
        graph: adjacency list (u -> list of v)
        deterministic: if True, processes available nodes in sorted order.

    Raises:
        ValueError: if a cycle is detected.
    """

    nodes: set[T] = set(graph.keys())
    for vs in graph.values():
        nodes.update(vs)

    indeg: dict[T, int] = {n: 0 for n in nodes}
    for u, vs in graph.items():
        for v in vs:
            indeg[v] += 1

    if deterministic:
        zero = deque(sorted([n for n, d in indeg.items() if d == 0]))
    else:
        zero = deque([n for n, d in indeg.items() if d == 0])

    out: list[T] = []

    while zero:
        u = zero.popleft()
        out.append(u)
        for v in graph.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                zero.append(v)
        if deterministic:
            zero = deque(sorted(zero))

    if len(out) != len(nodes):
        raise ValueError("cycle detected")

    return out
