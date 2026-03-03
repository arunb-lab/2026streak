"""Rerooting DP template for trees.

Rerooting computes a DP value for every choice of root in O(n) after defining
how to merge child contributions.

Typical examples:
- Sum of distances from each node to all others
- Best subtree values / farthest distance
- Counting paths with constraints

This module provides a generic function that runs a two-pass rerooting.

You supply:
- merge(a, b): associative combine of contributions
- add_node(acc, u): incorporate the current node into the accumulated value
  (often identity; depends on your DP)
- lift(child_value, u, v): transform DP from child v when seen from parent u

The function returns dp_all[u] for each u as root.
"""

from __future__ import annotations

from typing import Callable, TypeVar

T = TypeVar("T")


def rerooting(
    n: int,
    g: list[list[int]],
    root: int,
    identity: T,
    merge: Callable[[T, T], T],
    lift: Callable[[T, int, int], T],
    add_node: Callable[[T, int], T],
) -> list[T]:
    if n <= 0:
        raise ValueError("n must be positive")
    if not (0 <= root < n):
        raise IndexError("root out of range")

    parent = [-1] * n
    order: list[int] = []
    stack = [root]
    parent[root] = root
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if parent[v] != -1:
                continue
            parent[v] = u
            stack.append(v)

    if len(order) != n:
        raise ValueError("graph is not connected (not a single tree)")

    # dp_down[u] = merged contributions from children of u, with add_node applied.
    dp_down: list[T] = [identity for _ in range(n)]

    for u in reversed(order):
        acc = identity
        for v in g[u]:
            if v == parent[u]:
                continue
            acc = merge(acc, lift(dp_down[v], u, v))
        dp_down[u] = add_node(acc, u)

    # dp_all[u] is answer when rooted at u.
    dp_all: list[T] = [identity for _ in range(n)]
    dp_up: list[T] = [identity for _ in range(n)]
    dp_up[root] = identity

    for u in order:
        # Prepare prefix/suffix merges of lifted children contributions.
        children = [v for v in g[u] if v != parent[u]]
        m = len(children)
        pref = [identity] * (m + 1)
        suf = [identity] * (m + 1)
        for i in range(m):
            v = children[i]
            pref[i + 1] = merge(pref[i], lift(dp_down[v], u, v))
        for i in range(m - 1, -1, -1):
            v = children[i]
            suf[i] = merge(suf[i + 1], lift(dp_down[v], u, v))

        total = merge(dp_up[u], pref[m])
        dp_all[u] = add_node(total, u)

        for i, v in enumerate(children):
            # Contribution to child v coming from the "parent side":
            # combine dp_up[u] with all siblings of v, then incorporate u itself,
            # then lift across the edge (v <- u).
            without_v = merge(dp_up[u], merge(pref[i], suf[i + 1]))
            from_u = add_node(without_v, u)
            dp_up[v] = lift(from_u, v, u)

    return dp_all
