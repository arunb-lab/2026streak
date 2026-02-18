"""DSA - Binary Search: Classic Binary Search

Problem:
Given a sorted array of integers nums and an integer target, return the index of
target if it exists. Otherwise return -1.

Approach:
- Maintain a search interval [lo..hi]
- Repeatedly pick mid and shrink the interval

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def binary_search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([], 7) == -1
    print("ok")
