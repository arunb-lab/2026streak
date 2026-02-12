import pytest

from project.dsa.bellman_ford import bellman_ford


def test_bellman_ford_handles_negative_edges() -> None:
    # 0 -> 1 (1), 1 -> 2 (-2), 0 -> 2 (4)
    edges = [(0, 1, 1), (1, 2, -2), (0, 2, 4)]
    dist, neg_cycle = bellman_ford(3, edges, 0)

    assert neg_cycle is False
    assert dist[2] == -1.0


def test_bellman_ford_detects_negative_cycle() -> None:
    edges = [(0, 1, 1), (1, 2, -2), (2, 1, -2)]  # cycle 1<->2 is negative
    dist, neg_cycle = bellman_ford(3, edges, 0)
    assert neg_cycle is True
    assert dist[0] == 0.0


def test_bellman_ford_validates_inputs() -> None:
    with pytest.raises(ValueError):
        bellman_ford(0, [], 0)

    with pytest.raises(IndexError):
        bellman_ford(3, [], 99)
