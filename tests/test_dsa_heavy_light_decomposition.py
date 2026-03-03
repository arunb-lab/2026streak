from __future__ import annotations

import random

from project.dsa.heavy_light_decomposition import HeavyLightDecomposition


def _path_nodes(n: int, edges: list[tuple[int, int]], u: int, v: int) -> list[int]:
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    parent = [-1] * n
    stack = [u]
    parent[u] = u
    while stack:
        x = stack.pop()
        if x == v:
            break
        for y in g[x]:
            if parent[y] != -1:
                continue
            parent[y] = x
            stack.append(y)

    path = []
    cur = v
    while cur != u:
        path.append(cur)
        cur = parent[cur]
    path.append(u)
    return path


def test_hld_path_sum_matches_bruteforce() -> None:
    rng = random.Random(0)

    # Random tree via parent pointers.
    n = 30
    edges: list[tuple[int, int]] = []
    for v in range(1, n):
        p = rng.randrange(v)
        edges.append((p, v))

    hld = HeavyLightDecomposition(n, edges, root=0)

    # Node weights and base array.
    w = [rng.randint(-5, 5) for _ in range(n)]
    base = [0] * n
    for node in range(n):
        base[hld.pos[node]] = w[node]

    # Prefix sums over base (since we only need static range sum for this test).
    pref = [0]
    for x in base:
        pref.append(pref[-1] + x)

    def range_sum(l: int, r: int) -> int:
        return pref[r + 1] - pref[l]

    for _ in range(200):
        u = rng.randrange(n)
        v = rng.randrange(n)

        got = 0
        for l, r in hld.decompose_path(u, v):
            got += range_sum(l, r)

        path = _path_nodes(n, edges, u, v)
        want = sum(w[x] for x in path)
        assert got == want
