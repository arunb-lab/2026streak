import pytest

from project.dsa.fenwick_tree import FenwickTree


def test_fenwick_prefix_and_range_sum() -> None:
    ft = FenwickTree.from_list([1, 2, 3, 4])

    assert ft.prefix_sum(0) == 0
    assert ft.prefix_sum(1) == 1
    assert ft.prefix_sum(4) == 10

    assert ft.range_sum(0, 4) == 10
    assert ft.range_sum(1, 3) == 5
    assert ft.range_sum(3, 4) == 4

    with pytest.raises(ValueError):
        ft.prefix_sum(5)

    with pytest.raises(ValueError):
        ft.range_sum(-1, 2)


def test_fenwick_add_updates_sums() -> None:
    ft = FenwickTree.from_list([0, 0, 0])
    ft.add(1, 5)
    ft.add(2, 2)

    assert ft.prefix_sum(3) == 7
    assert ft.range_sum(0, 2) == 5

    with pytest.raises(IndexError):
        ft.add(5, 1)


def test_find_by_prefix_order_statistics() -> None:
    # counts (non-negative)
    ft = FenwickTree.from_list([2, 0, 3, 1])
    # expanded multiset indexes: [0,0,2,2,2,3]
    assert ft.find_by_prefix(1) == 0
    assert ft.find_by_prefix(2) == 0
    assert ft.find_by_prefix(3) == 2
    assert ft.find_by_prefix(5) == 2
    assert ft.find_by_prefix(6) == 3

    with pytest.raises(ValueError):
        ft.find_by_prefix(0)
    with pytest.raises(ValueError):
        ft.find_by_prefix(7)
