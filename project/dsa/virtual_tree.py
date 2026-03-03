"""Virtual Tree construction.

Given a rooted tree and a subset of nodes S, the *virtual tree* is the minimal
(tree) subgraph that connects all nodes in S, obtained by adding the LCAs of
consecutive nodes in DFS order.

Use cases:
- Many problems on subsets of nodes (DP on marked nodes) in O(|S| log |S|).

This module provides a small helper that requires an LCA structure and Euler
entry times (tin).

Refs:
- Common competitive programming technique.
"""

from __future__ import annotations

from dataclasses import dataclass

from project.dsa.lca_binary_lifting import LCA


@dataclass(frozen=True)
class VirtualTree:
    root: int
    nodes: list[int]
    adj: dict[int, list[int]]  # directed parent -> children


class VirtualTreeBuilder:
    def __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0) -> None:
        self.n = n
        self.root = root
        self.edges = edges
        self.lca = LCA(n, edges, root=root)

        g: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        self.tin = [-1] * n
        self.parent = [-1] * n
        t = 0

        stack: list[tuple[int, int, int]] = [(root, -1, 0)]  # (u, p, state) state: 0 enter, 1 exit
        it_index = [0] * n
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                self.parent[u] = p
                self.tin[u] = t
                t += 1
                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v == p:
                        continue
                    stack.append((v, u, 0))
            else:
                # exit; nothing needed for virtual tree
                pass

    def build(self, nodes: list[int]) -> VirtualTree:
        if not nodes:
            raise ValueError("nodes must be non-empty")

        uniq = sorted(set(nodes), key=lambda x: self.tin[x])

        # Add LCAs of consecutive nodes in DFS order.
        all_nodes = uniq[:]
        for i in range(len(uniq) - 1):
            all_nodes.append(self.lca.lca(uniq[i], uniq[i + 1]))
        all_nodes = sorted(set(all_nodes), key=lambda x: self.tin[x])

        # Stack-based construction.
        adj: dict[int, list[int]] = {v: [] for v in all_nodes}
        st: list[int] = []

        def is_ancestor(a: int, b: int) -> bool:
            # With only tin we can still test ancestor by climbing using LCA.
            return self.lca.lca(a, b) == a

        for v in all_nodes:
            if not st:
                st.append(v)
                continue
            while st and not is_ancestor(st[-1], v):
                st.pop()
            if not st:
                # Should not happen; root should be ancestor of all.
                st.append(v)
                continue
            adj[st[-1]].append(v)
            st.append(v)

        root = all_nodes[0]
        return VirtualTree(root=root, nodes=all_nodes, adj=adj)
