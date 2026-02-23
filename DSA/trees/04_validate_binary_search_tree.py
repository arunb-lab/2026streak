"""DSA - Trees: Validate Binary Search Tree

Problem:
Given the root of a binary tree, determine if it is a valid binary search tree.
A BST is valid if:
- left subtree values < node.val
- right subtree values > node.val
- both subtrees are also BSTs

Approach (DFS with bounds):
- Carry (low, high) bounds down the recursion
- Each node must satisfy low < val < high

Time: O(n)
Space: O(h) recursion depth
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def is_valid_bst(root: TreeNode | None) -> bool:
    def dfs(node: TreeNode | None, low: int | None, high: int | None) -> bool:
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, None, None)


if __name__ == "__main__":
    assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3))) is True
    assert is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) is False
    assert is_valid_bst(None) is True
    print("ok")
