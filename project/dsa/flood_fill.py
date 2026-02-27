"""Flood fill (DFS/BFS on a grid).

Problem:
Given an m x n integer image, a start cell (sr, sc), and a newColor,
"flood fill" the connected component of the start cell (4-directionally)
that has the same original color, replacing it with newColor.

Time: O(m*n) worst case
Space: O(m*n) worst case (stack/queue)
"""

from __future__ import annotations

from collections import deque


def flood_fill(image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
    """Return image after flood-filling from (sr, sc).

    Note: This mutates and returns the same `image` list.
    """

    rows = len(image)
    cols = len(image[0]) if rows else 0
    if rows == 0 or cols == 0:
        return image

    orig = image[sr][sc]
    if orig == new_color:
        return image

    q: deque[tuple[int, int]] = deque([(sr, sc)])
    image[sr][sc] = new_color

    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig:
                image[nr][nc] = new_color
                q.append((nr, nc))

    return image
