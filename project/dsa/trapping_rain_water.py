"""Trapping Rain Water (LeetCode 42).

Problem:
Given `height` where each element represents an elevation map bar of width 1,
compute how much water it can trap after raining.

Approach (two pointers):
Maintain left/right pointers and the best (max) wall seen so far from each side.
Water above a bar is limited by the smaller of the two side maxima.
When left_max <= right_max, the left side is the bottleneck, so we can finalize
water at `left` and move left forward; symmetrically for the right.

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations


def trap_rain_water(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        hl = height[left]
        hr = height[right]
        if hl < 0 or hr < 0:
            raise ValueError("heights must be non-negative")

        if left_max <= right_max:
            left_max = max(left_max, hl)
            water += left_max - hl
            left += 1
        else:
            right_max = max(right_max, hr)
            water += right_max - hr
            right -= 1

    return water
