"""DSA - Queue: Implement Queue using Two Stacks

Goal:
Implement a FIFO queue using only stack operations.

Approach:
Maintain two stacks:
- in_stack: pushes go here
- out_stack: pops/peeks come from here
When out_stack is empty and we need to pop/peek, pour all items from in_stack to
out_stack, reversing order.

Amortized Time:
- push: O(1)
- pop/peek: O(1) amortized (each element moves stacks at most once)
Space: O(n)
"""

from __future__ import annotations


class MyQueue:
    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def _pour_if_needed(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def pop(self) -> int:
        self._pour_if_needed()
        if not self._out:
            raise IndexError("pop from empty queue")
        return self._out.pop()

    def peek(self) -> int:
        self._pour_if_needed()
        if not self._out:
            raise IndexError("peek from empty queue")
        return self._out[-1]

    def empty(self) -> bool:
        return (not self._in) and (not self._out)


if __name__ == "__main__":
    q = MyQueue()
    assert q.empty() is True
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    assert q.pop() == 2
    assert q.empty() is True
    print("ok")
