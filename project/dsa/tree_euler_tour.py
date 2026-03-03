"""Euler tour (tin/tout) for rooted trees.

Computes:
- parent[u]
- depth[u]
- tin[u] (entry time)
- tout[u] (exit time, exclusive)
- order: nodes in entry order

Useful for:
- subtree queries (subtree of u corresponds to order[tin[u]:tout[u]])
- ancestor checks: u is ancestor of v iff tin[u] <= tin[v] < tout[u]

Runs in O(n).
"""

from __future__ import annotations


def euler_tour(
    n: int, edges: list[tuple[int, int]], root: int = 0
) -> tuple[list[int], list[int], list[int], list[int], list[int]]:
    if n <= 0:
        raise ValueError("n must be positive")
    if not (0 <= root < n):
        raise IndexError("root out of range")

    g: list[list[int]] = [[] for _ in range(n)]
    for a, b in edges:
        if not (0 <= a < n and 0 <= b < n):
            raise IndexError("edge node out of range")
        g[a].append(b)
        g[b].append(a)

    parent = [-1] * n
    depth = [-1] * n
    tin = [-1] * n
    tout = [-1] * n
    order: list[int] = []

    t = 0
    stack: list[tuple[int, int, int]] = [(root, -1, 0)]  # (u, p, state) 0 enter, 1 exit
    depth[root] = 0

    while stack:
        u, p, state = stack.pop()
        if state == 0:
            parent[u] = p
            tin[u] = t
            t += 1
            order.append(u)
            stack.append((u, p, 1))
            for v in reversed(g[u]):
                if v == p:
                    continue
                depth[v] = depth[u] + 1
                stack.append((v, u, 0))
        else:
            tout[u] = t

    if any(x == -1 for x in tin):
        raise ValueError("graph is not connected (not a single tree)")

    return parent, depth, tin, tout, order


def is_ancestor(u: int, v: int, tin: list[int], tout: list[int]) -> bool:
    return tin[u] <= tin[v] < tout[u]
