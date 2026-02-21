"""Minimum Size Subarray Sum (LeetCode 209).

Problem:
Given an array of positive integers `nums` and a positive integer `target`, return
the minimal length of a contiguous subarray of which the sum is greater than or
equal to `target`. If there is no such subarray, return 0.

Approach (sliding window):
Because all numbers are positive, expanding the right end of the window can only
increase the sum. We keep a window [left, right] whose sum we track; whenever
the sum is >= target, we try to shrink from the left to minimize length.

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations


def min_subarray_len(target: int, nums: list[int]) -> int:
    if target <= 0:
        raise ValueError("target must be positive")

    best = float("inf")
    window_sum = 0
    left = 0

    for right, x in enumerate(nums):
        if x <= 0:
            raise ValueError("nums must contain only positive integers")

        window_sum += x
        while window_sum >= target and left <= right:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else int(best)
