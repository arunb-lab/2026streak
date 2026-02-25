"""DSA - Binary Search: Search in Rotated Sorted Array

Problem:
You are given a rotated sorted array of distinct integers and a target.
Return the index of target if it exists, else -1.

Approach:
- Standard binary search variant.
- At each step, determine which half [l..m] or [m..r] is sorted.
- Narrow the search range based on where the target must lie.

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def search_rotated(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            # left half is sorted
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            # right half is sorted
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    print("ok")
