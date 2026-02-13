import pytest

from project.dsa.prim_mst import prim_mst


def test_prim_mst_total_weight() -> None:
    # Same graph as in Kruskal test, but as adjacency list (undirected, both ways).
    edges = [
        ("A", "B", 4),
        ("A", "H", 8),
        ("B", "C", 8),
        ("B", "H", 11),
        ("C", "D", 7),
        ("C", "F", 4),
        ("C", "I", 2),
        ("D", "E", 9),
        ("D", "F", 14),
        ("E", "F", 10),
        ("F", "G", 2),
        ("G", "H", 1),
        ("G", "I", 6),
        ("H", "I", 7),
    ]

    g: dict[str, list[tuple[str, float]]] = {}
    for u, v, w in edges:
        g.setdefault(u, []).append((v, w))
        g.setdefault(v, []).append((u, w))

    total, mst = prim_mst(g, start="A")

    assert total == 37.0
    assert len(mst) == 8


def test_prim_mst_disconnected_raises() -> None:
    g = {"A": [("B", 1.0)], "B": [("A", 1.0)], "C": []}
    with pytest.raises(ValueError):
        prim_mst(g, start="A")
