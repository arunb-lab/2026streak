from project.dsa.binary_tree import TreeNode, build_tree_level_order
from project.dsa.validate_bst import is_valid_bst


def test_is_valid_bst_true() -> None:
    #      5
    #    /   \
    #   3     7
    #  / \   / \
    # 2  4  6   8
    root = build_tree_level_order([5, 3, 7, 2, 4, 6, 8])
    assert is_valid_bst(root) is True


def test_is_valid_bst_false_due_to_subtree_value() -> None:
    #      5
    #    /   \
    #   1     4
    #        / \
    #       3   6
    # This is invalid because 3 is in the right subtree of 5.
    root = build_tree_level_order([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst(root) is False


def test_is_valid_bst_duplicates_invalid() -> None:
    # duplicates violate strict BST condition
    root = TreeNode(2, left=TreeNode(2), right=TreeNode(3))
    assert is_valid_bst(root) is False


def test_is_valid_bst_empty() -> None:
    assert is_valid_bst(None) is True
