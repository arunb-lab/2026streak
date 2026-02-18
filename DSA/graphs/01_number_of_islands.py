"""DSA - Graphs: Number of Islands

Problem:
Given an m x n 2D grid of '1's (land) and '0's (water), return the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically.

Approach (DFS flood-fill):
- Iterate through all cells
- When a '1' is found, increment count and DFS to mark all reachable '1's as '0'

Time: O(m*n)
Space: O(m*n) worst-case recursion / stack
"""

from __future__ import annotations


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands


if __name__ == "__main__":
    g1 = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    assert num_islands(g1) == 1

    g2 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(g2) == 3
    print("ok")
