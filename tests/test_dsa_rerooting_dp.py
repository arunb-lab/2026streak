from __future__ import annotations

import random

from project.dsa.rerooting_dp import rerooting


def test_rerooting_sum_of_distances_random_tree() -> None:
    # Compute sum of distances from each node to all others.
    rng = random.Random(0)
    n = 25
    edges: list[tuple[int, int]] = []
    g = [[] for _ in range(n)]
    for v in range(1, n):
        p = rng.randrange(v)
        edges.append((p, v))
        g[p].append(v)
        g[v].append(p)

    # We'll compute for each root u:
    # dp value is pair (subtree_size, sum_dist_to_nodes_in_component)
    # merge: component union
    # lift from child to parent: distances + size
    # add_node: include u itself (size+1, sum unchanged)

    def merge(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (a[0] + b[0], a[1] + b[1])

    def lift(child: tuple[int, int], u: int, v: int) -> tuple[int, int]:
        size, dist_sum = child
        # All nodes in child's component are 1 further from u than from v.
        return (size, dist_sum + size)

    def add_node(acc: tuple[int, int], u: int) -> tuple[int, int]:
        size, dist_sum = acc
        return (size + 1, dist_sum)

    dp_all = rerooting(
        n=n,
        g=g,
        root=0,
        identity=(0, 0),
        merge=merge,
        lift=lift,
        add_node=add_node,
    )

    # Brute force distances by BFS from each node.
    def brute(u: int) -> int:
        dist = [-1] * n
        dist[u] = 0
        q = [u]
        for x in q:
            for y in g[x]:
                if dist[y] != -1:
                    continue
                dist[y] = dist[x] + 1
                q.append(y)
        return sum(dist)

    for u in range(n):
        assert dp_all[u][1] == brute(u)
