import pytest

from project.dsa.lca_binary_lifting import LCA


def test_lca_basic_tree() -> None:
    # Tree:
    # 0
    # ├─1
    # │ ├─3
    # │ └─4
    # └─2
    #   └─5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    lca = LCA(6, edges, root=0)

    assert lca.lca(3, 4) == 1
    assert lca.lca(3, 5) == 0
    assert lca.lca(2, 5) == 2
    assert lca.lca(0, 5) == 0


def test_kth_ancestor() -> None:
    edges = [(0, 1), (1, 2), (2, 3)]
    lca = LCA(4, edges, root=0)

    assert lca.kth_ancestor(3, 0) == 3
    assert lca.kth_ancestor(3, 1) == 2
    assert lca.kth_ancestor(3, 2) == 1
    assert lca.kth_ancestor(3, 3) == 0
    assert lca.kth_ancestor(3, 4) == -1


def test_lca_rejects_disconnected_graph() -> None:
    with pytest.raises(ValueError):
        LCA(3, [(0, 1)], root=0)
