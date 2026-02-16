"""DSA - Queue: Moving Average from Data Stream

Problem:
Given a stream of integers and a window size, return the moving average of the
last `size` values after each insertion.

Approach:
Maintain a queue (here: list + head index) and a running sum.
- push: append value, add to sum
- if window exceeds size: drop oldest, subtract from sum
- average = sum / current_window_length

Time: O(1) amortized per next()
Space: O(size)
"""

from __future__ import annotations


class MovingAverage:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("size must be positive")
        self._size = size
        self._q: list[int] = []
        self._head = 0
        self._sum = 0

    def next(self, val: int) -> float:
        self._q.append(val)
        self._sum += val

        # shrink window
        while (len(self._q) - self._head) > self._size:
            self._sum -= self._q[self._head]
            self._head += 1

        # optional compaction to avoid unbounded growth
        if self._head > 64 and self._head * 2 > len(self._q):
            self._q = self._q[self._head :]
            self._head = 0

        window_len = len(self._q) - self._head
        return self._sum / window_len


if __name__ == "__main__":
    m = MovingAverage(3)
    assert abs(m.next(1) - 1.0) < 1e-9
    assert abs(m.next(10) - 5.5) < 1e-9
    assert abs(m.next(3) - 4.6666666667) < 1e-6
    assert abs(m.next(5) - 6.0) < 1e-9
    print("ok")
