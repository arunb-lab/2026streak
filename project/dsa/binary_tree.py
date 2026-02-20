from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class TreeNode(Generic[T]):
    """Simple binary tree node.

    This intentionally matches the common LeetCode-style structure while keeping
    helpers for constructing and serializing trees for tests.
    """

    val: T
    left: Optional[TreeNode[T]] = None
    right: Optional[TreeNode[T]] = None


def build_tree_level_order(values: Iterable[Optional[T]]) -> Optional[TreeNode[T]]:
    """Build a binary tree from a level-order iterable.

    Args:
        values: Level-order values where `None` means "no node".

    Returns:
        The root node or None.

    Example:
        [3, 9, 20, None, None, 15, 7] builds:
                3
              /   \
             9    20
                 /  \
                15   7
    """

    it = iter(values)
    try:
        first = next(it)
    except StopIteration:
        return None

    if first is None:
        return None

    root: TreeNode[T] = TreeNode(first)
    q: deque[TreeNode[T]] = deque([root])

    while q:
        node = q.popleft()

        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            q.append(node.left)

        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            q.append(node.right)

    return root


def iter_level_order(root: Optional[TreeNode[T]]) -> Iterator[Optional[T]]:
    """Iterate a tree in level order, including trailing structure.

    This is mainly useful for tests/debugging.
    """

    if root is None:
        return
        yield  # pragma: no cover

    q: deque[Optional[TreeNode[T]]] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            yield None
            continue

        yield node.val
        # Always enqueue children; caller may trim trailing Nones if desired.
        q.append(node.left)
        q.append(node.right)


def to_level_order_list(root: Optional[TreeNode[T]]) -> list[Optional[T]]:
    out = list(iter_level_order(root))
    # Trim trailing Nones for a canonical representation.
    while out and out[-1] is None:
        out.pop()
    return out
