from project.dsa.binary_tree import build_tree_level_order
from project.dsa.binary_tree_level_order import level_order


def test_level_order_basic() -> None:
    root = build_tree_level_order([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_level_order_empty() -> None:
    assert level_order(None) == []
