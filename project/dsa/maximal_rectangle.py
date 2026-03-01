"""Maximal Rectangle in a Binary Matrix (LeetCode 85).

Problem:
Given a rows x cols binary matrix filled with '0' and '1', find the largest
rectangle containing only '1's and return its area.

Approach:
Treat each row as the base of a histogram:
- Maintain `heights[c]`: consecutive number of '1's ending at current row.
- For each row, compute largest rectangle area in the histogram via a
  monotonic increasing stack.

Time:  O(R*C)
Space: O(C)
"""

from __future__ import annotations


def _largest_rectangle_histogram(heights: list[int]) -> int:
    best = 0
    stack: list[tuple[int, int]] = []  # (start_index, height)

    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            start0, h0 = stack.pop()
            best = max(best, h0 * (i - start0))
            start = start0
        if not stack or stack[-1][1] < h:
            stack.append((start, h))
    return best


def maximal_rectangle(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    best = 0

    for row in matrix:
        if len(row) != cols:
            raise ValueError("matrix must be rectangular")
        for c, ch in enumerate(row):
            if ch == "1":
                heights[c] += 1
            elif ch == "0":
                heights[c] = 0
            else:
                raise ValueError("matrix entries must be '0' or '1'")

        best = max(best, _largest_rectangle_histogram(heights))

    return best
