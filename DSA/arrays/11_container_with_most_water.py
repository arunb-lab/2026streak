"""DSA - Arrays: Container With Most Water

Problem:
Given n non-negative integers height[i] where each represents a point at x=i,
find two lines that together with the x-axis form a container that holds the most
water.

Approach (two pointers):
- Start with left=0, right=n-1
- Area = min(h[l], h[r]) * (r-l)
- Move the pointer at the smaller height inward (only that can improve)

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def max_area(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    best = 0

    while l < r:
        h = min(height[l], height[r])
        best = max(best, h * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("ok")
