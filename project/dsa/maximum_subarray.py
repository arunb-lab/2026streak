"""Maximum subarray (Kadane's algorithm).

Problem:
Given an integer array nums, find the contiguous subarray with the largest sum
and return its sum.

Approach (Kadane):
Maintain the best subarray sum ending at the current index.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def maximum_subarray_sum(nums: list[int]) -> int:
    """Return the maximum sum of any non-empty contiguous subarray.

    Raises:
        ValueError: if nums is empty.
    """

    if not nums:
        raise ValueError("nums must be non-empty")

    best_ending_here = nums[0]
    best_overall = nums[0]

    for x in nums[1:]:
        best_ending_here = max(x, best_ending_here + x)
        best_overall = max(best_overall, best_ending_here)

    return best_overall
