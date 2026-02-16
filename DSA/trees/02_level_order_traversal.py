"""DSA - Trees: Level Order Traversal (BFS)

Problem:
Return the level-order traversal of a binary tree: nodes level by level.

Approach:
Breadth-first search using a queue.
Track current level size to separate levels.

Time: O(n)
Space: O(w) where w is max width of the tree
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    q: list[TreeNode] = [root]
    head = 0
    out: list[list[int]] = []

    while head < len(q):
        level_len = len(q) - head
        level: list[int] = []
        for _ in range(level_len):
            node = q[head]
            head += 1
            level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        out.append(level)

        # compact occasionally
        if head > 64 and head * 2 > len(q):
            q = q[head:]
            head = 0

    return out


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert level_order(None) == []
    print("ok")
