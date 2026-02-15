from project.dsa.hashing_two_sum import two_sum_indices


def test_two_sum_indices_found() -> None:
    nums = [2, 7, 11, 15]
    res = two_sum_indices(nums, 9)
    assert res is not None
    i, j = res
    assert nums[i] + nums[j] == 9


def test_two_sum_indices_with_duplicates() -> None:
    nums = [3, 3]
    assert two_sum_indices(nums, 6) == (0, 1)


def test_two_sum_indices_not_found() -> None:
    assert two_sum_indices([1, 2, 3], 999) is None
