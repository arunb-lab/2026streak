"""DSA - Stack: Largest Rectangle in Histogram

Problem:
Given an array heights where heights[i] is the height of a bar in a histogram
(width=1), return the area of the largest rectangle.

Approach (monotonic increasing stack):
- Keep stack of indices with increasing heights.
- When current height is smaller, pop indices and compute area where popped
  height is the limiting height.
- Use a sentinel 0 height at the end to flush the stack.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def largest_rectangle_area(heights: list[int]) -> int:
    stack: list[int] = []  # indices
    best = 0

    for i in range(len(heights) + 1):
        curr_h = heights[i] if i < len(heights) else 0

        while stack and curr_h < heights[stack[-1]]:
            h = heights[stack.pop()]
            left_smaller = stack[-1] if stack else -1
            width = i - left_smaller - 1
            best = max(best, h * width)

        stack.append(i)

    return best


if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([]) == 0
    print("ok")
