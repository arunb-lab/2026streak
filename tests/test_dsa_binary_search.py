from project.dsa.binary_search import lower_bound, search_rotated_sorted


def test_lower_bound() -> None:
    nums = [1, 2, 2, 4, 10]
    assert lower_bound(nums, 0) == 0
    assert lower_bound(nums, 2) == 1
    assert lower_bound(nums, 3) == 3
    assert lower_bound(nums, 10) == 4
    assert lower_bound(nums, 11) == 5


def test_search_rotated_sorted() -> None:
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated_sorted(nums, 0) == 4
    assert search_rotated_sorted(nums, 3) == -1
    assert search_rotated_sorted([1], 1) == 0
    assert search_rotated_sorted([1], 0) == -1
