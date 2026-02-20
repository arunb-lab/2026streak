import pytest

from project.dsa.binary_tree import build_tree_level_order
from project.dsa.bst_kth_smallest import kth_smallest


def test_kth_smallest_basic() -> None:
    root = build_tree_level_order([5, 3, 7, 2, 4, 6, 8])
    assert kth_smallest(root, 1) == 2
    assert kth_smallest(root, 3) == 4
    assert kth_smallest(root, 7) == 8


def test_kth_smallest_validation() -> None:
    root = build_tree_level_order([2, 1, 3])

    with pytest.raises(ValueError):
        kth_smallest(root, 0)

    with pytest.raises(IndexError):
        kth_smallest(root, 999)
