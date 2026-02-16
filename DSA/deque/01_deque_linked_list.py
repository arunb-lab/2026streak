"""DSA - Deque: Doubly Linked List Deque

Goal:
Implement a double-ended queue (deque) supporting push/pop from both ends in
O(1) time.

Approach:
Use a doubly-linked list with sentinel head/tail nodes to simplify edge cases.

Time: O(1) per operation
Space: O(n)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Node:
    val: int
    prev: "_Node | None" = None
    nxt: "_Node | None" = None


class Deque:
    def __init__(self) -> None:
        self._head = _Node(0)  # sentinel
        self._tail = _Node(0)  # sentinel
        self._head.nxt = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def append_left(self, x: int) -> None:
        first = self._head.nxt
        assert first is not None
        node = _Node(x, prev=self._head, nxt=first)
        self._head.nxt = node
        first.prev = node
        self._size += 1

    def append_right(self, x: int) -> None:
        last = self._tail.prev
        assert last is not None
        node = _Node(x, prev=last, nxt=self._tail)
        last.nxt = node
        self._tail.prev = node
        self._size += 1

    def pop_left(self) -> int:
        if self.is_empty():
            raise IndexError("pop_left from empty deque")
        first = self._head.nxt
        assert first is not None and first is not self._tail
        second = first.nxt
        assert second is not None
        self._head.nxt = second
        second.prev = self._head
        self._size -= 1
        return first.val

    def pop_right(self) -> int:
        if self.is_empty():
            raise IndexError("pop_right from empty deque")
        last = self._tail.prev
        assert last is not None and last is not self._head
        before = last.prev
        assert before is not None
        before.nxt = self._tail
        self._tail.prev = before
        self._size -= 1
        return last.val

    def peek_left(self) -> int:
        if self.is_empty():
            raise IndexError("peek_left from empty deque")
        first = self._head.nxt
        assert first is not None and first is not self._tail
        return first.val

    def peek_right(self) -> int:
        if self.is_empty():
            raise IndexError("peek_right from empty deque")
        last = self._tail.prev
        assert last is not None and last is not self._head
        return last.val


if __name__ == "__main__":
    d = Deque()
    d.append_right(2)
    d.append_left(1)
    d.append_right(3)
    assert len(d) == 3
    assert d.peek_left() == 1
    assert d.peek_right() == 3
    assert d.pop_left() == 1
    assert d.pop_right() == 3
    assert d.pop_left() == 2
    assert d.is_empty()
    print("ok")
