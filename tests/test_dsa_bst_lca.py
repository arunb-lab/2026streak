from project.dsa.binary_tree import build_tree_level_order
from project.dsa.bst_lca import lca_bst


def test_lca_bst_basic() -> None:
    # BST:
    #        6
    #      /   \
    #     2     8
    #    / \   / \
    #   0   4 7   9
    #      / \
    #     3   5
    root = build_tree_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    assert lca_bst(root, 2, 8).val == 6
    assert lca_bst(root, 2, 4).val == 2
    assert lca_bst(root, 3, 5).val == 4


def test_lca_bst_empty() -> None:
    assert lca_bst(None, 1, 2) is None
