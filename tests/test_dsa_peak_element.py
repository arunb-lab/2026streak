import pytest

from project.dsa.peak_element import find_peak_element


def _is_peak(nums: list[int], i: int) -> bool:
    left = nums[i - 1] if i - 1 >= 0 else float("-inf")
    right = nums[i + 1] if i + 1 < len(nums) else float("-inf")
    return nums[i] > left and nums[i] > right


def test_find_peak_element_basic() -> None:
    nums = [1, 2, 3, 1]
    i = find_peak_element(nums)
    assert _is_peak(nums, i)


def test_find_peak_element_multiple_peaks() -> None:
    nums = [1, 2, 1, 3, 5, 6, 4]
    i = find_peak_element(nums)
    assert _is_peak(nums, i)


def test_find_peak_element_singleton() -> None:
    assert find_peak_element([7]) == 0


def test_find_peak_element_empty_raises() -> None:
    with pytest.raises(ValueError):
        find_peak_element([])
