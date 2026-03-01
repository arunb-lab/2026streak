"""Set Matrix Zeroes (LeetCode 73).

Problem:
Given an m x n integer matrix, if an element is 0, set its entire row and column
to 0s.

Requirement:
Do it in-place with O(1) additional space.

Approach:
Use first row and first column as marker storage.

Time:  O(m*n)
Space: O(1)
"""

from __future__ import annotations


def set_matrix_zeroes(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    if any(len(row) != cols for row in matrix):
        raise ValueError("matrix must be rectangular")

    first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
    first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

    # Mark zeros using first row/col.
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Zero marked rows/cols.
    for r in range(1, rows):
        if matrix[r][0] == 0:
            for c in range(1, cols):
                matrix[r][c] = 0

    for c in range(1, cols):
        if matrix[0][c] == 0:
            for r in range(1, rows):
                matrix[r][c] = 0

    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
