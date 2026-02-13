import pytest

from project.dsa.quickselect import quickselect


def test_quickselect_kth_smallest() -> None:
    nums = [7, 2, 1, 8, 6, 3, 5, 4]
    assert quickselect(nums[:], 0) == 1
    assert quickselect(nums[:], 3) == 4
    assert quickselect(nums[:], 7) == 8


def test_quickselect_duplicates() -> None:
    nums = [5, 1, 5, 2, 5]
    assert quickselect(nums[:], 0) == 1
    assert quickselect(nums[:], 1) == 2


def test_quickselect_invalid_k() -> None:
    with pytest.raises(IndexError):
        quickselect([1, 2, 3], -1)
    with pytest.raises(IndexError):
        quickselect([1, 2, 3], 3)
