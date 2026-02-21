"""Search in Rotated Sorted Array (LeetCode 33).

Problem:
Given a rotated sorted array of distinct integers `nums` and an integer `target`,
return its index; otherwise return -1.

Approach (modified binary search):
At each step, at least one of the halves is sorted. We decide whether `target`
lies in the sorted half; if yes, search there, else search the other half.

Time:  O(log n)
Space: O(1)
"""

from __future__ import annotations


def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Left half sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
