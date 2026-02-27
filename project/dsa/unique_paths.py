"""Unique paths (grid DP).

Problem:
A robot is located at the top-left corner of an m x n grid.
It can only move either down or right.
How many unique paths are there to reach the bottom-right corner?

Approach:
1D DP where dp[c] is number of ways to reach current row, column c.

Time: O(m*n)
Space: O(n)
"""

from __future__ import annotations


def unique_paths(m: int, n: int) -> int:
    """Return number of unique paths in an m x n grid.

    Args:
        m: number of rows (>= 1)
        n: number of columns (>= 1)

    Raises:
        ValueError: if m or n are <= 0.
    """

    if m <= 0 or n <= 0:
        raise ValueError("m and n must be positive")

    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[-1]
