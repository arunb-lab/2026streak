"""DSA - Stack (Monotonic): Daily Temperatures

Problem:
Given a list of daily temperatures, return a list where ans[i] is the number of
days to wait until a warmer temperature. If none, ans[i] = 0.

Approach (monotonic decreasing stack):
- Maintain stack of indices with decreasing temperatures
- When we see a warmer temp, resolve previous indices

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def daily_temperatures(temps: list[int]) -> list[int]:
    ans = [0] * len(temps)
    stack: list[int] = []  # indices, temps[stack] strictly decreasing

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    print("ok")
