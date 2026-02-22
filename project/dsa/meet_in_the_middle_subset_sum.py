"""Meet-in-the-middle subset sum.

Useful when n is ~40 and classic DP over sum is too large.

This module provides:
- subset_sum_exists(nums, target)

Time: O(2^(n/2) * n)
Space: O(2^(n/2))
"""

from __future__ import annotations

from bisect import bisect_left


def _subset_sums(nums: list[int]) -> list[int]:
    sums = [0]
    for x in nums:
        sums += [s + x for s in sums]
    return sums


def subset_sum_exists(nums: list[int], target: int) -> bool:
    """Return True if some subset of nums sums to target."""

    n = len(nums)
    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]

    a = _subset_sums(left)
    b = _subset_sums(right)
    b.sort()

    for s in a:
        need = target - s
        i = bisect_left(b, need)
        if i < len(b) and b[i] == need:
            return True
    return False
