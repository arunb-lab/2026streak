"""DSA - Trees: Maximum Depth of Binary Tree

Problem:
Given the root of a binary tree, return its maximum depth.

Approach (DFS recursion):
- Depth of a node = 1 + max(depth(left), depth(right))

Time: O(n)
Space: O(h) recursion stack where h is tree height
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    #    3
    #   / \
    #  9  20
    #     / \
    #    15  7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1
    print("ok")
