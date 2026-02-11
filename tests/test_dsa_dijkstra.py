import pytest

from project.dsa.dijkstra import dijkstra


def test_dijkstra_dist_and_path() -> None:
    g = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    res = dijkstra(g, "A")
    assert res.dist["D"] == 4.0  # A->B->C->D
    assert res.path_to("D") == ["A", "B", "C", "D"]


def test_dijkstra_rejects_negative_weights() -> None:
    with pytest.raises(ValueError):
        dijkstra({"A": [("B", -1)]}, "A")
