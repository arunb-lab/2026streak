"""DSA - Binary Search: Find Minimum in Rotated Sorted Array

Problem:
Given a rotated sorted array of unique integers, find the minimum element.

Approach:
Binary search on the inflection point.
- Compare mid with rightmost element.
- If nums[mid] > nums[hi], minimum is to the right of mid.
- Else, minimum is at mid or to the left.

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def find_min(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    print("ok")
