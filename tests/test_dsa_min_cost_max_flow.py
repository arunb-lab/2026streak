import pytest

from project.dsa.min_cost_max_flow import MinCostMaxFlow, min_cost_max_flow


def test_min_cost_flow_small() -> None:
    # 0 -> 1 (cap 2, cost 1)
    # 0 -> 2 (cap 1, cost 0)
    # 2 -> 1 (cap 1, cost 0)
    # 1 -> 3 (cap 3, cost 0)
    # 2 -> 3 (cap 1, cost 5)
    # Best: send 3 units from 0 to 3.
    edges = [
        (0, 1, 2, 1),
        (0, 2, 1, 0),
        (2, 1, 1, 0),
        (1, 3, 3, 0),
        (2, 3, 1, 5),
    ]
    flow, cost = min_cost_max_flow(4, edges, 0, 3)
    assert flow == 3
    # Route 1 unit 0->2->1->3 cost 0, and 2 units 0->1->3 cost 2.
    assert cost == 2


def test_validation() -> None:
    with pytest.raises(ValueError):
        MinCostMaxFlow(0)

    m = MinCostMaxFlow(2)
    with pytest.raises(ValueError):
        m.add_edge(0, 1, -1, 0)

    with pytest.raises(IndexError):
        m.add_edge(0, 99, 1, 0)
