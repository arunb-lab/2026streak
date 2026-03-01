"""Minimum Path Sum (LeetCode 64).

Problem:
Given an m x n grid filled with non-negative numbers, find a path from top-left
to bottom-right which minimizes the sum of all numbers along its path.
You can only move either down or right at any point.

Approach:
DP with rolling row.

Time:  O(m*n)
Space: O(n)
"""

from __future__ import annotations


def min_path_sum(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        raise ValueError("grid must be non-empty")

    rows = len(grid)
    cols = len(grid[0])
    if any(len(row) != cols for row in grid):
        raise ValueError("grid must be rectangular")

    dp = [0] * cols
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[c] = grid[r][c]
            elif r == 0:
                dp[c] = dp[c - 1] + grid[r][c]
            elif c == 0:
                dp[c] = dp[c] + grid[r][c]
            else:
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]

    return dp[-1]
