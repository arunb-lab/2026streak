"""Daily Temperatures (LeetCode 739).

Problem:
Given a list of daily temperatures `temps`, return an array `ans` such that
`ans[i]` is the number of days you have to wait after day i to get a warmer
temperature. If there is no future day for which this is possible, keep 0.

Approach (monotonic decreasing stack):
Maintain a stack of indices with strictly decreasing temperatures.
When we see a new temperature that is higher than the one at the stack top,
we pop indices and fill their answer with the distance to the current index.

Time:  O(n)
Space: O(n)
"""

from __future__ import annotations


def daily_temperatures(temps: list[int]) -> list[int]:
    n = len(temps)
    ans = [0] * n
    stack: list[int] = []  # indices

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
