"""Longest Increasing Path in a Matrix (LeetCode 329).

Problem:
Given an integer matrix, return the length of the longest increasing path.
You may move in 4 directions (up/down/left/right). You may not move diagonally
or move outside the boundary.

Approach:
DFS + memoization (DP on DAG induced by increasing edges).

Time:  O(m*n)
Space: O(m*n) for memo + recursion stack
"""

from __future__ import annotations


def longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    if any(len(row) != cols for row in matrix):
        raise ValueError("matrix must be rectangular")

    memo = [[0] * cols for _ in range(rows)]

    def dfs(r: int, c: int) -> int:
        if memo[r][c] != 0:
            return memo[r][c]

        best = 1
        v = matrix[r][c]
        if r > 0 and matrix[r - 1][c] > v:
            best = max(best, 1 + dfs(r - 1, c))
        if r + 1 < rows and matrix[r + 1][c] > v:
            best = max(best, 1 + dfs(r + 1, c))
        if c > 0 and matrix[r][c - 1] > v:
            best = max(best, 1 + dfs(r, c - 1))
        if c + 1 < cols and matrix[r][c + 1] > v:
            best = max(best, 1 + dfs(r, c + 1))

        memo[r][c] = best
        return best

    ans = 0
    for r in range(rows):
        for c in range(cols):
            ans = max(ans, dfs(r, c))
    return ans
