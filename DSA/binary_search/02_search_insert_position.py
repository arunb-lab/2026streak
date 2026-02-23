"""DSA - Binary Search: Search Insert Position

Problem:
Given a sorted array of distinct integers and a target value, return the index if
target is found. If not, return the index where it would be inserted in order.

Approach:
Classic binary search for the first index with nums[i] >= target.

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)  # hi is exclusive
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    print("ok")
