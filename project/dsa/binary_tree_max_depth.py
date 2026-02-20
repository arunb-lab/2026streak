from __future__ import annotations

from collections import deque
from typing import Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


def max_depth_dfs(root: Optional[TreeNode[T]]) -> int:
    """Maximum depth (height) of a binary tree (DFS)."""

    if root is None:
        return 0
    return 1 + max(max_depth_dfs(root.left), max_depth_dfs(root.right))


def max_depth_bfs(root: Optional[TreeNode[T]]) -> int:
    """Maximum depth using BFS level counting."""

    if root is None:
        return 0

    depth = 0
    q: deque[TreeNode[T]] = deque([root])
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    return depth
