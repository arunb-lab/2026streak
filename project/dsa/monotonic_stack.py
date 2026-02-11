"""Monotonic stack patterns.

A monotonic stack keeps elements in increasing/decreasing order to answer
"next greater/smaller" and "span" type problems efficiently.
"""

from __future__ import annotations


def next_greater_elements(nums: list[int]) -> list[int | None]:
    """For each index i, return the next element to the right that is greater.

    If none exists, value is None.

    Time:  O(n)
    Space: O(n)
    """

    res: list[int | None] = [None] * len(nums)
    stack: list[int] = []  # indices with decreasing values

    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            j = stack.pop()
            res[j] = x
        stack.append(i)

    return res


def largest_rectangle_histogram(heights: list[int]) -> int:
    """Largest rectangle area in a histogram.

    Classic monotonic increasing stack of indices.

    Time:  O(n)
    Space: O(n)
    """

    best = 0
    stack: list[int] = []  # indices of increasing heights

    for i in range(len(heights) + 1):
        cur = 0 if i == len(heights) else heights[i]

        while stack and heights[stack[-1]] > cur:
            h = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            width = i - left
            best = max(best, h * width)

        stack.append(i)

    return best
