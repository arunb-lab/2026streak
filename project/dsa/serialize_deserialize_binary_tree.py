"""Serialize and Deserialize Binary Tree (LeetCode 297).

We provide a small, test-friendly codec:
- serialize(root) -> str using BFS (level-order) with "#" for nulls
- deserialize(data) -> TreeNode

The format is stable and round-trips: deserialize(serialize(root)) is equivalent
(up to structure) for any finite binary tree.

Time:  O(n)
Space: O(n)
"""

from __future__ import annotations

from collections import deque
from typing import Optional

from project.dsa.binary_tree import TreeNode


def serialize(root: Optional[TreeNode[int]]) -> str:
    if root is None:
        return ""

    out: list[str] = []
    q: deque[Optional[TreeNode[int]]] = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            out.append("#")
            continue

        out.append(str(node.val))
        q.append(node.left)
        q.append(node.right)

    # Trim trailing nulls to keep strings short but deterministic.
    while out and out[-1] == "#":
        out.pop()

    return ",".join(out)


def deserialize(data: str) -> Optional[TreeNode[int]]:
    if data == "":
        return None

    parts = data.split(",")
    if not parts or parts[0] == "#":
        return None

    root = TreeNode(int(parts[0]))
    q: deque[TreeNode[int]] = deque([root])

    i = 1
    while q and i < len(parts):
        node = q.popleft()

        if i < len(parts) and parts[i] != "#":
            node.left = TreeNode(int(parts[i]))
            q.append(node.left)
        i += 1

        if i < len(parts) and parts[i] != "#":
            node.right = TreeNode(int(parts[i]))
            q.append(node.right)
        i += 1

    return root
