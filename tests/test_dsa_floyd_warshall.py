from math import inf

from project.dsa.floyd_warshall import floyd_warshall, has_negative_cycle


def test_floyd_warshall_basic() -> None:
    graph = {
        "A": [("B", 3), ("C", 8), ("E", -4)],
        "B": [("D", 1), ("E", 7)],
        "C": [("B", 4)],
        "D": [("A", 2), ("C", -5)],
        "E": [("D", 6)],
    }

    dist = floyd_warshall(graph)

    assert dist["A"]["A"] == 0
    assert dist["A"]["D"] == 2  # A->E->D
    assert dist["A"]["C"] == -3  # A->E->D->C
    assert dist["C"]["E"] == 3  # C->B->D->A->E
    assert not has_negative_cycle(dist)


def test_floyd_warshall_unreachable() -> None:
    graph = {"A": [("B", 1)], "C": []}
    dist = floyd_warshall(graph)

    assert dist["A"]["C"] == inf
    assert dist["C"]["B"] == inf


def test_negative_cycle_detection() -> None:
    graph = {
        "A": [("B", 1)],
        "B": [("C", 1)],
        "C": [("A", -3)],
    }
    dist = floyd_warshall(graph)
    assert has_negative_cycle(dist)
