from project.dsa.graph_bipartite import is_bipartite


def test_is_bipartite_true() -> None:
    # 0-1-2-3 is bipartite
    graph = [
        [1],
        [0, 2],
        [1, 3],
        [2],
    ]
    assert is_bipartite(graph) is True


def test_is_bipartite_false_odd_cycle() -> None:
    # Triangle 0-1-2-0 is not bipartite
    graph = [
        [1, 2],
        [0, 2],
        [0, 1],
    ]
    assert is_bipartite(graph) is False


def test_is_bipartite_disconnected() -> None:
    graph = [
        [1],
        [0],
        [3],
        [2],
        [],
    ]
    assert is_bipartite(graph) is True
