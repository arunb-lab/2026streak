from __future__ import annotations

import random

from project.dsa.hopcroft_karp import HopcroftKarp


def _bruteforce_max_matching(n_left: int, n_right: int, edges: list[tuple[int, int]]) -> int:
    # Slow brute force for tiny graphs: try all matchings via recursion.
    g = [[] for _ in range(n_left)]
    for u, v in edges:
        g[u].append(v)

    used_r = [False] * n_right

    def rec(u: int) -> int:
        if u == n_left:
            return 0
        best = rec(u + 1)  # skip u
        for v in g[u]:
            if not used_r[v]:
                used_r[v] = True
                best = max(best, 1 + rec(u + 1))
                used_r[v] = False
        return best

    return rec(0)


def test_hopcroft_karp_small() -> None:
    hk = HopcroftKarp(3, 3)
    hk.add_edge(0, 0)
    hk.add_edge(0, 1)
    hk.add_edge(1, 1)
    hk.add_edge(2, 2)
    assert hk.max_matching() == 3


def test_hopcroft_karp_random_tiny_matches_bruteforce() -> None:
    rng = random.Random(0)
    for _ in range(100):
        n_left = rng.randint(0, 6)
        n_right = rng.randint(0, 6)
        edges: list[tuple[int, int]] = []
        hk = HopcroftKarp(n_left, n_right)
        for u in range(n_left):
            for v in range(n_right):
                if rng.random() < 0.3:
                    edges.append((u, v))
                    hk.add_edge(u, v)
        assert hk.max_matching() == _bruteforce_max_matching(n_left, n_right, edges)
