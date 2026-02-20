from __future__ import annotations

from collections import deque
from typing import Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


def level_order(root: Optional[TreeNode[T]]) -> list[list[T]]:
    """Return level-order traversal as list of levels."""

    if root is None:
        return []

    out: list[list[T]] = []
    q: deque[TreeNode[T]] = deque([root])

    while q:
        n = len(q)
        level: list[T] = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        out.append(level)

    return out
