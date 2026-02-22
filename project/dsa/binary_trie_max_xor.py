"""Binary trie for maximum XOR queries.

This module implements:
- maximum XOR of any pair in a list
- maximum XOR of a query value against inserted values

Typical use: problems like "Maximum XOR of Two Numbers in an Array".
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Node:
    child0: int = -1
    child1: int = -1


class BinaryTrie:
    def __init__(self, bit_width: int = 31) -> None:
        if bit_width <= 0:
            raise ValueError("bit_width must be positive")
        self.bit_width = bit_width
        self.nodes: list[_Node] = [_Node()]
        self.size = 0

    def insert(self, x: int) -> None:
        if x < 0:
            raise ValueError("only non-negative integers supported")
        v = 0
        for b in range(self.bit_width - 1, -1, -1):
            bit = (x >> b) & 1
            if bit == 0:
                nxt = self.nodes[v].child0
                if nxt == -1:
                    self.nodes.append(_Node())
                    nxt = len(self.nodes) - 1
                    self.nodes[v].child0 = nxt
            else:
                nxt = self.nodes[v].child1
                if nxt == -1:
                    self.nodes.append(_Node())
                    nxt = len(self.nodes) - 1
                    self.nodes[v].child1 = nxt
            v = nxt
        self.size += 1

    def best_xor(self, x: int) -> int:
        """Return maximum XOR achievable with x and any inserted value."""

        if self.size == 0:
            raise ValueError("trie is empty")
        if x < 0:
            raise ValueError("only non-negative integers supported")

        v = 0
        ans = 0
        for b in range(self.bit_width - 1, -1, -1):
            bit = (x >> b) & 1
            want = 1 - bit
            nxt = self.nodes[v].child1 if want == 1 else self.nodes[v].child0
            if nxt == -1:
                nxt = self.nodes[v].child1 if bit == 1 else self.nodes[v].child0
            else:
                ans |= 1 << b
            v = nxt
        return ans


def max_xor_pair(nums: list[int]) -> int:
    """Maximum XOR over all pairs in nums.

    Returns 0 for lists with <2 elements.
    """

    if len(nums) < 2:
        return 0

    bw = max(1, max(nums).bit_length())
    t = BinaryTrie(bit_width=bw)

    t.insert(nums[0])
    best = 0
    for x in nums[1:]:
        best = max(best, t.best_xor(x))
        t.insert(x)
    return best
