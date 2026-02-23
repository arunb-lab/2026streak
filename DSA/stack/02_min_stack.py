"""DSA - Stack: Min Stack

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Approach (two stacks):
- data stack holds all values
- mins stack holds the minimum so far at each depth

Time: O(1) per operation
Space: O(n)
"""

from __future__ import annotations


class MinStack:
    def __init__(self) -> None:
        self._data: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        self._data.append(val)
        if not self._mins:
            self._mins.append(val)
        else:
            self._mins.append(min(val, self._mins[-1]))

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty stack")
        self._mins.pop()
        return self._data.pop()

    def top(self) -> int:
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("min from empty stack")
        return self._mins[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    assert s.pop() == -3
    assert s.top() == 0
    assert s.get_min() == -2
    print("ok")
