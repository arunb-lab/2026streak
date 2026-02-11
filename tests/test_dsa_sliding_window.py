import pytest

from project.dsa.sliding_window import longest_substring_k_distinct, max_sum_subarray_k


def test_max_sum_subarray_k() -> None:
    assert max_sum_subarray_k([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_subarray_k([-1, -2, -3], 1) == -1

    with pytest.raises(ValueError):
        max_sum_subarray_k([1, 2, 3], 0)
    with pytest.raises(ValueError):
        max_sum_subarray_k([1, 2, 3], 4)


def test_longest_substring_k_distinct() -> None:
    assert longest_substring_k_distinct("eceba", 2) == 3  # "ece"
    assert longest_substring_k_distinct("aa", 1) == 2
    assert longest_substring_k_distinct("", 2) == 0
    assert longest_substring_k_distinct("abc", 0) == 0
