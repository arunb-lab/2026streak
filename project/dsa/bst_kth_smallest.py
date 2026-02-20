from __future__ import annotations

from typing import Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


def kth_smallest(root: Optional[TreeNode[T]], k: int) -> T:
    """Return the k-th smallest element in a BST (1-indexed).

    Raises:
        ValueError: if k <= 0.
        IndexError: if the tree has fewer than k nodes.
    """

    if k <= 0:
        raise ValueError("k must be >= 1")

    st: list[TreeNode[T]] = []
    cur = root
    seen = 0

    while cur is not None or st:
        while cur is not None:
            st.append(cur)
            cur = cur.left

        node = st.pop()
        seen += 1
        if seen == k:
            return node.val

        cur = node.right

    raise IndexError("k is larger than the number of nodes")
