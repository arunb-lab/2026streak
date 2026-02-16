"""DSA - Queue: Number of Recent Calls

Problem (LeetCode 933 style):
Design a class that counts pings in the last 3000 ms.
Given a time t (in ms, strictly increasing), return the number of pings in
[t-3000, t].

Approach:
Maintain a monotonic time queue of ping timestamps.
On each ping:
- append t
- pop from left while oldest < t - 3000
- answer is queue length

Time: O(1) amortized per ping
Space: O(w) where w is number of pings in last 3000 ms
"""

from __future__ import annotations


class RecentCounter:
    def __init__(self) -> None:
        self._q: list[int] = []
        self._head = 0

    def ping(self, t: int) -> int:
        self._q.append(t)
        lower = t - 3000
        while self._head < len(self._q) and self._q[self._head] < lower:
            self._head += 1

        # compact occasionally
        if self._head > 64 and self._head * 2 > len(self._q):
            self._q = self._q[self._head :]
            self._head = 0

        return len(self._q) - self._head


if __name__ == "__main__":
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
    print("ok")
