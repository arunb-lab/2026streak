"""DSA - Trees: Lowest Common Ancestor (Binary Tree)

Problem:
Given a binary tree and two nodes p and q (values assumed unique), return their
lowest common ancestor (LCA).

Approach (DFS recursion):
- If current node is None: return None
- If current node matches p or q: return node
- Recurse left and right
  - If both sides return non-null -> current is LCA
  - Else return whichever side is non-null

Time: O(n)
Space: O(h) recursion stack
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def lowest_common_ancestor(root: TreeNode | None, p: int, q: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == p or root.val == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    return left if left is not None else right


if __name__ == "__main__":
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    root = TreeNode(
        3,
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(2, TreeNode(7), TreeNode(4)),
        ),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )

    assert lowest_common_ancestor(root, 5, 1).val == 3
    assert lowest_common_ancestor(root, 5, 4).val == 5
    assert lowest_common_ancestor(root, 6, 4).val == 5
    print("ok")
