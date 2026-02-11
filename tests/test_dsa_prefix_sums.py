import pytest

from project.dsa.prefix_sums import PrefixSums, subarray_sum_equals_k


def test_prefix_sums_range_sum() -> None:
    nums = [1, 2, 3, 4]
    ps = PrefixSums.from_list(nums)

    assert ps.range_sum(0, 1) == 1
    assert ps.range_sum(0, 4) == 10
    assert ps.range_sum(1, 3) == 5

    with pytest.raises(ValueError):
        ps.range_sum(-1, 2)
    with pytest.raises(ValueError):
        ps.range_sum(3, 2)
    with pytest.raises(ValueError):
        ps.range_sum(0, 5)


def test_subarray_sum_equals_k() -> None:
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2  # [1,2], [3]
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3
