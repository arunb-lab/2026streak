import pytest

from project.dsa.graph_traversal import bfs_shortest_path, topo_sort_dfs


def test_bfs_shortest_path() -> None:
    g = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    assert bfs_shortest_path(g, "A", "D") in (["A", "B", "D"], ["A", "C", "D"])
    assert bfs_shortest_path(g, "A", "A") == ["A"]
    assert bfs_shortest_path(g, "D", "A") is None


def test_topo_sort_dfs() -> None:
    g = {
        "cook": ["eat"],
        "shop": ["cook"],
        "eat": [],
    }
    order = topo_sort_dfs(g)
    assert order.index("shop") < order.index("cook") < order.index("eat")

    with pytest.raises(ValueError):
        topo_sort_dfs({"A": ["B"], "B": ["A"]})
