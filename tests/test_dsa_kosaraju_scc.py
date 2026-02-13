from project.dsa.kosaraju_scc import kosaraju_scc


def _as_sets(sccs: list[list[str]]) -> list[frozenset[str]]:
    return sorted([frozenset(c) for c in sccs], key=lambda s: (len(s), sorted(s)))


def test_kosaraju_scc_components() -> None:
    # Classic example.
    g = {
        "A": ["B"],
        "B": ["C", "E"],
        "C": ["A", "D"],
        "D": ["E"],
        "E": ["F"],
        "F": ["D"],
        "G": ["F", "H"],
        "H": ["I"],
        "I": ["G"],
    }

    sccs = kosaraju_scc(g)

    assert _as_sets(sccs) == _as_sets(
        [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
        ]
    )


def test_kosaraju_single_node_graph() -> None:
    assert kosaraju_scc({"A": []}) == [["A"]]
