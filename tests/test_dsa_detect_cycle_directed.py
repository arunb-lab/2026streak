from project.dsa.detect_cycle_directed import has_cycle_directed


def test_has_cycle_directed_false_dag() -> None:
    graph = [
        [1, 2],
        [3],
        [3],
        [],
    ]
    assert has_cycle_directed(graph) is False


def test_has_cycle_directed_true_simple_cycle() -> None:
    graph = [
        [1],
        [2],
        [0],
    ]
    assert has_cycle_directed(graph) is True


def test_has_cycle_directed_disconnected() -> None:
    graph = [
        [1],
        [],
        [3],
        [2],
    ]
    assert has_cycle_directed(graph) is True
