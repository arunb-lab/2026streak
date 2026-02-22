from project.dsa.tarjan_scc import condensation_dag, tarjan_scc, topo_sort_dag


def _as_sets(comps: list[list[str]]) -> set[frozenset[str]]:
    return {frozenset(c) for c in comps}


def test_tarjan_scc_matches_known_example() -> None:
    # Same classic example used in Kosaraju test.
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

    res = tarjan_scc(g)

    assert _as_sets(res.components) == {
        frozenset({"A", "B", "C"}),
        frozenset({"D", "E", "F"}),
        frozenset({"G", "H", "I"}),
    }


def test_tarjan_scc_includes_nodes_only_in_adjacency() -> None:
    g = {"A": ["B"]}  # B is not a key
    res = tarjan_scc(g)
    assert _as_sets(res.components) == {frozenset({"A"}), frozenset({"B"})}


def test_condensation_dag_is_acyclic() -> None:
    g = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A", "D"],
        "D": [],
    }

    scc = tarjan_scc(g)
    dag = condensation_dag(g, scc)

    order = topo_sort_dag(dag)
    assert set(order) == set(dag.keys())
