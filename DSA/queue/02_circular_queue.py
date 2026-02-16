"""DSA - Queue: Circular Queue (Ring Buffer)

Goal:
Implement a fixed-capacity queue with O(1) enqueue/dequeue using a ring buffer.

Key idea:
- Use an array of size k
- Track head index and current size
- tail index is (head + size) % k

Time: O(1) per operation
Space: O(k)
"""

from __future__ import annotations


class CircularQueue:
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

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        tail = (self._head + self._size) % self._k
        self._buf[tail] = value
        self._size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self._buf[self._head] = None
        self._head = (self._head + 1) % self._k
        self._size -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("front from empty queue")
        x = self._buf[self._head]
        assert x is not None
        return x

    def rear(self) -> int:
        if self.is_empty():
            raise IndexError("rear from empty queue")
        tail = (self._head + self._size - 1) % self._k
        x = self._buf[tail]
        assert x is not None
        return x


if __name__ == "__main__":
    q = CircularQueue(3)
    assert q.enqueue(1)
    assert q.enqueue(2)
    assert q.enqueue(3)
    assert not q.enqueue(4)
    assert q.front() == 1
    assert q.rear() == 3
    assert q.dequeue()
    assert q.enqueue(4)
    assert q.rear() == 4
    assert q.front() == 2
    print("ok")
