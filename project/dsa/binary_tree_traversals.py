from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from project.dsa.binary_tree import TreeNode

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Traversals(Generic[T]):
    preorder: list[T]
    inorder: list[T]
    postorder: list[T]


def traversals_recursive(root: Optional[TreeNode[T]]) -> Traversals[T]:
    """Return preorder/inorder/postorder traversals (recursive)."""

    pre: list[T] = []
    ino: list[T] = []
    post: list[T] = []

    def dfs(node: Optional[TreeNode[T]]) -> None:
        if node is None:
            return
        pre.append(node.val)
        dfs(node.left)
        ino.append(node.val)
        dfs(node.right)
        post.append(node.val)

    dfs(root)
    return Traversals(preorder=pre, inorder=ino, postorder=post)


def inorder_iterative(root: Optional[TreeNode[T]]) -> list[T]:
    """Iterative inorder traversal using an explicit stack."""

    out: list[T] = []
    st: list[TreeNode[T]] = []
    cur = root

    while cur is not None or st:
        while cur is not None:
            st.append(cur)
            cur = cur.left

        node = st.pop()
        out.append(node.val)
        cur = node.right

    return out


def preorder_iterative(root: Optional[TreeNode[T]]) -> list[T]:
    """Iterative preorder traversal."""

    if root is None:
        return []

    out: list[T] = []
    st: list[TreeNode[T]] = [root]
    while st:
        node = st.pop()
        out.append(node.val)
        # Right first so left is processed first.
        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)

    return out


def postorder_iterative(root: Optional[TreeNode[T]]) -> list[T]:
    """Iterative postorder traversal.

    Uses a classic two-stack technique (implemented as one stack + output list).
    """

    if root is None:
        return []

    out: list[T] = []
    st: list[TreeNode[T]] = [root]
    while st:
        node = st.pop()
        out.append(node.val)
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)

    out.reverse()
    return out
