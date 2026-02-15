from project.dsa.hashing_subarray_sum_indices import first_subarray_sum_k


def test_first_subarray_sum_k_found() -> None:
    nums = [1, 2, 3]
    l, r = first_subarray_sum_k(nums, 3) or (-1, -1)
    assert nums[l:r] in ([1, 2], [3])
    assert sum(nums[l:r]) == 3


def test_first_subarray_sum_k_with_negatives() -> None:
    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    res = first_subarray_sum_k(nums, 7)
    assert res is not None
    l, r = res
    assert sum(nums[l:r]) == 7


def test_first_subarray_sum_k_not_found() -> None:
    assert first_subarray_sum_k([1, 2, 3], 999) is None


def test_first_subarray_sum_k_empty() -> None:
    assert first_subarray_sum_k([], 0) is None
