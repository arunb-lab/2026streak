import pytest

from project.dsa.dinic_max_flow import Dinic, max_flow


def test_max_flow_small_network() -> None:
    # Classic example:
    # s=0, t=3
    # 0->1 (3), 0->2 (2)
    # 1->2 (5), 1->3 (2)
    # 2->3 (3)
    edges = [(0, 1, 3), (0, 2, 2), (1, 2, 5), (1, 3, 2), (2, 3, 3)]
    assert max_flow(4, edges, 0, 3) == 5.0


def test_dinic_validation() -> None:
    with pytest.raises(ValueError):
        Dinic(0)

    d = Dinic(2)
    with pytest.raises(ValueError):
        d.add_edge(0, 1, -1)

    with pytest.raises(IndexError):
        d.add_edge(0, 99, 1)

    with pytest.raises(IndexError):
        d.max_flow(0, 99)


def test_max_flow_same_source_sink_is_zero() -> None:
    d = Dinic(3)
    d.add_edge(0, 1, 10)
    assert d.max_flow(1, 1) == 0.0
