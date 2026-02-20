from __future__ import annotations

from typing import Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


def lca_bst(root: Optional[TreeNode[T]], p: T, q: T) -> Optional[TreeNode[T]]:
    """Lowest common ancestor in a BST by leveraging ordering.

    Args:
        root: BST root.
        p: value of first node.
        q: value of second node.

    Returns:
        The LCA node, or None if root is None.

    Notes:
        This function finds the split point where p and q diverge. It does not
        verify that p and q actually exist in the tree; if you need that, add an
        existence check.
    """

    cur = root

    lo, hi = (p, q) if p <= q else (q, p)

    while cur is not None:
        if cur.val < lo:
            cur = cur.right
        elif cur.val > hi:
            cur = cur.left
        else:
            return cur

    return None
