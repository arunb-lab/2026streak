"""Find a peak element.

Problem:
Given an array nums, a peak element is an element that is strictly greater than
its neighbors.
Return the index of any peak element.
Assume nums[-1] = nums[n] = -infinity.

Approach:
Binary search on the slope:
- If nums[mid] < nums[mid+1], peak is to the right.
- Else, peak is to the left (including mid).

Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


def find_peak_element(nums: list[int]) -> int:
    """Return index of a peak element.

    Raises:
        ValueError: if nums is empty.
    """

    if not nums:
        raise ValueError("nums must be non-empty")

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
