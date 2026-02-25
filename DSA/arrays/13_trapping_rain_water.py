"""DSA - Arrays: Trapping Rain Water

Problem:
Given n non-negative integers representing elevation map where width of each bar is 1,
compute how much water it can trap after raining.

Approach (two pointers):
- Maintain pointers l, r.
- Track left_max and right_max.
- Always move the side with smaller max boundary; trapped water is boundary - height.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def trap_rain_water(height: list[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while l < r:
        if height[l] <= height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1

    return water


if __name__ == "__main__":
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap_rain_water([4, 2, 0, 3, 2, 5]) == 9
    assert trap_rain_water([]) == 0
    print("ok")
