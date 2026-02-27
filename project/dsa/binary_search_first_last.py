"""Find first and last position of element in sorted array.

Problem:
Given a sorted array of integers nums and an integer target, return the
starting and ending position of target in nums.
If target is not found, return (-1, -1).

Approach:
Use two binary searches (lower_bound / upper_bound).

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def _lower_bound(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _upper_bound(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def first_last_position(nums: list[int], target: int) -> tuple[int, int]:
    """Return (first_index, last_index) for target, or (-1, -1) if absent."""

    left = _lower_bound(nums, target)
    if left == len(nums) or nums[left] != target:
        return (-1, -1)

    right_exclusive = _upper_bound(nums, target)
    return (left, right_exclusive - 1)
