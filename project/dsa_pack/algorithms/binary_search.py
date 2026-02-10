from __future__ import annotations

from typing import List, Optional


def binary_search(nums: List[int], target: int) -> Optional[int]:
    """Return index of target in sorted nums, or None.

    Time: O(log n)
    Space: O(1)
    """

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def lower_bound(nums: List[int], target: int) -> int:
    """Return the leftmost index to insert target in sorted nums."""

    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
