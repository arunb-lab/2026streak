from project.dsa.binary_tree import build_tree_level_order, to_level_order_list


def test_build_tree_level_order_roundtrip() -> None:
    vals = [3, 9, 20, None, None, 15, 7]
    root = build_tree_level_order(vals)
    assert to_level_order_list(root) == vals


def test_build_tree_level_order_empty() -> None:
    assert build_tree_level_order([]) is None
    assert build_tree_level_order([None]) is None
