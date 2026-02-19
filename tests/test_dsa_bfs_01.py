from math import inf

import pytest

from project.dsa.bfs_01 import bfs_01


def test_bfs_01_shortest_paths() -> None:
    # 0 -> 1 (0), 0 -> 2 (1), 1 -> 2 (0), 2 -> 3 (1)
    edges = [(0, 1, 0), (0, 2, 1), (1, 2, 0), (2, 3, 1)]
    dist = bfs_01(4, edges, 0)

    assert dist[0] == 0.0
    assert dist[1] == 0.0
    assert dist[2] == 0.0  # 0->1->2
    assert dist[3] == 1.0  # 0->1->2->3


def test_bfs_01_unreachable() -> None:
    dist = bfs_01(3, [(0, 1, 1)], 0)
    assert dist[2] == inf


def test_bfs_01_validation() -> None:
    with pytest.raises(ValueError):
        bfs_01(0, [], 0)

    with pytest.raises(IndexError):
        bfs_01(3, [], 3)

    with pytest.raises(ValueError):
        bfs_01(2, [(0, 1, 2)], 0)

    with pytest.raises(IndexError):
        bfs_01(2, [(0, 9, 1)], 0)
