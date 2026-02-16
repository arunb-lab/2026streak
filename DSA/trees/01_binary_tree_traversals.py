"""DSA - Trees: Binary Tree Traversals (Iterative)

Covers:
- Preorder (root, left, right)
- Inorder  (left, root, right)
- Postorder(left, right, root)

Approach:
- Preorder: stack, process node then push right then left
- Inorder:   stack + pointer, push left spine then visit, then go right
- Postorder: two stacks OR one stack with visited flag; here: one stack + visited

Time: O(n)
Space: O(h) where h is tree height
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    out: list[int] = []
    stack: list[TreeNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return out


def inorder(root: TreeNode | None) -> list[int]:
    out: list[int] = []
    stack: list[TreeNode] = []
    cur = root
    while cur is not None or stack:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def postorder(root: TreeNode | None) -> list[int]:
    out: list[int] = []
    if root is None:
        return out

    # (node, visited_children)
    stack: list[tuple[TreeNode, bool]] = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if visited:
            out.append(node.val)
            continue
        stack.append((node, True))
        if node.right is not None:
            stack.append((node.right, False))
        if node.left is not None:
            stack.append((node.left, False))

    return out


if __name__ == "__main__":
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert preorder(root) == [1, 2, 4, 5, 3]
    assert inorder(root) == [4, 2, 5, 1, 3]
    assert postorder(root) == [4, 5, 2, 3, 1]
    print("ok")
