from __future__ import annotations

from typing import Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


def is_valid_bst(root: Optional[TreeNode[T]]) -> bool:
    """Check if a binary tree is a valid BST.

    A valid BST requires:
    - all keys in left subtree < node.val
    - all keys in right subtree > node.val
    - both subtrees are valid

    Notes:
        This implementation assumes values are totally ordered (support < and >).
    """

    def ok(node: Optional[TreeNode[T]], low: Optional[T], high: Optional[T]) -> bool:
        if node is None:
            return True
        if low is not None and not (node.val > low):
            return False
        if high is not None and not (node.val < high):
            return False
        return ok(node.left, low, node.val) and ok(node.right, node.val, high)

    return ok(root, None, None)
