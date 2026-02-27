import pytest

from project.dsa.maximum_subarray import maximum_subarray_sum


def test_maximum_subarray_sum_basic() -> None:
    assert maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maximum_subarray_sum([1]) == 1
    assert maximum_subarray_sum([5, 4, -1, 7, 8]) == 23


def test_maximum_subarray_sum_all_negative() -> None:
    assert maximum_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_maximum_subarray_sum_empty_raises() -> None:
    with pytest.raises(ValueError):
        maximum_subarray_sum([])
