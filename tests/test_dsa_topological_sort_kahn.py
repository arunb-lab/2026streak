import pytest

from project.dsa.topological_sort import kahn_topo_sort


def test_kahn_topo_sort_orders_dependencies() -> None:
    g = {
        "shop": ["cook"],
        "cook": ["eat"],
        "eat": [],
    }
    order = kahn_topo_sort(g)
    assert order.index("shop") < order.index("cook") < order.index("eat")


def test_kahn_topo_sort_includes_isolated_nodes() -> None:
    g = {
        "a": ["b"],
        "b": [],
        "c": [],
    }
    order = kahn_topo_sort(g)
    assert set(order) == {"a", "b", "c"}


def test_kahn_topo_sort_cycle_detected() -> None:
    with pytest.raises(ValueError):
        kahn_topo_sort({"A": ["B"], "B": ["A"]})
