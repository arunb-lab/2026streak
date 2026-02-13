"""Longest Increasing Subsequence (LIS).

Provides O(n log n) length computation using the classic "tails" method.

- lis_length: strictly increasing subsequence length

Time:  O(n log n)
Space: O(n)
"""

from __future__ import annotations

import bisect


def lis_length(nums: list[int]) -> int:
    tails: list[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
