from project.dsa.kruskal_mst import kruskal_mst


def test_kruskal_mst_connected_graph() -> None:
    # Example graph (undirected), edges listed once.
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

    total, mst = kruskal_mst(edges)

    assert len(mst) == 8  # V-1 edges for 9 nodes
    assert total == 37.0


def test_kruskal_minimum_spanning_forest_when_disconnected() -> None:
    edges = [("A", "B", 1), ("C", "D", 2)]
    total, mst = kruskal_mst(edges)
    assert len(mst) == 2
    assert total == 3.0
