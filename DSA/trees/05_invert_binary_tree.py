"""DSA - Trees: Invert Binary Tree

Problem:
Invert a binary tree (swap left/right children for all nodes).

Approach:
DFS recursion: swap children and recurse.

Time: O(n)
Space: O(h)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


if __name__ == "__main__":
    #      4
    #     / \
    #    2   7
    #   / \ / \
    #  1  3 6  9
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)),
    )
    assert preorder(root) == [4, 2, 1, 3, 7, 6, 9]
    invert_tree(root)
    assert preorder(root) == [4, 7, 9, 6, 2, 3, 1]
    print("ok")
