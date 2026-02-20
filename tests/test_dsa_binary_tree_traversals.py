from project.dsa.binary_tree import build_tree_level_order
from project.dsa.binary_tree_traversals import (
    inorder_iterative,
    postorder_iterative,
    preorder_iterative,
    traversals_recursive,
)


def test_traversals_match_between_recursive_and_iterative() -> None:
    # Tree: [1, None, 2, 3]
    #    1
    #     \
    #      2
    #     /
    #    3
    root = build_tree_level_order([1, None, 2, 3])

    rec = traversals_recursive(root)

    assert preorder_iterative(root) == rec.preorder
    assert inorder_iterative(root) == rec.inorder
    assert postorder_iterative(root) == rec.postorder


def test_empty_tree_traversals() -> None:
    assert preorder_iterative(None) == []
    assert inorder_iterative(None) == []
    assert postorder_iterative(None) == []
    assert traversals_recursive(None).preorder == []
