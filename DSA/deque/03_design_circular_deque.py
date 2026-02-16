"""DSA - Deque: Design Circular Deque

Goal:
Implement a fixed-capacity deque supporting insert/delete at both ends in O(1).

Approach:
Use a ring buffer of size k with head index and size.
- front index is head
- rear index is (head + size - 1) % k

Time: O(1) per operation
Space: O(k)
"""

from __future__ import annotations


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        if k <= 0:
            raise ValueError("k must be positive")
        self._buf: list[int | None] = [None] * k
        self._k = k
        self._head = 0
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._k

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        self._head = (self._head - 1) % self._k
        self._buf[self._head] = value
        self._size += 1
        return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        tail = (self._head + self._size) % self._k
        self._buf[tail] = value
        self._size += 1
        return True

    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        self._buf[self._head] = None
        self._head = (self._head + 1) % self._k
        self._size -= 1
        return True

    def delete_last(self) -> bool:
        if self.is_empty():
            return False
        tail = (self._head + self._size - 1) % self._k
        self._buf[tail] = None
        self._size -= 1
        return True

    def get_front(self) -> int:
        if self.is_empty():
            raise IndexError("get_front from empty deque")
        x = self._buf[self._head]
        assert x is not None
        return x

    def get_rear(self) -> int:
        if self.is_empty():
            raise IndexError("get_rear from empty deque")
        tail = (self._head + self._size - 1) % self._k
        x = self._buf[tail]
        assert x is not None
        return x


if __name__ == "__main__":
    d = MyCircularDeque(3)
    assert d.insert_last(1)
    assert d.insert_last(2)
    assert d.insert_front(3)
    assert not d.insert_front(4)
    assert d.get_rear() == 2
    assert d.is_full() is True
    assert d.delete_last()
    assert d.insert_front(4)
    assert d.get_front() == 4
    print("ok")
