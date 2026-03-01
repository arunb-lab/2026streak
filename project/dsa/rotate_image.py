"""Rotate Image (LeetCode 48).

Problem:
Given an n x n 2D matrix representing an image, rotate it 90 degrees clockwise
in-place.

Approach:
- Transpose (swap matrix[r][c] with matrix[c][r])
- Reverse each row

Time:  O(n^2)
Space: O(1)
"""

from __future__ import annotations


def rotate_image(matrix: list[list[int]]) -> None:
    n = len(matrix)
    if n == 0:
        return
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")

    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(n):
        matrix[r].reverse()
