from project.dsa.binary_tree import build_tree_level_order, to_level_order_list
from project.dsa.serialize_deserialize_binary_tree import deserialize, serialize


def test_serialize_deserialize_roundtrip() -> None:
    root = build_tree_level_order([1, 2, 3, None, None, 4, 5])
    s = serialize(root)
    root2 = deserialize(s)
    assert to_level_order_list(root2) == [1, 2, 3, None, None, 4, 5]


def test_serialize_empty() -> None:
    assert serialize(None) == ""
    assert deserialize("") is None
