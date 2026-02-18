"""DSA - Dynamic Programming: Climbing Stairs

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Approach (bottom-up DP with O(1) space):
- ways[i] = ways[i-1] + ways[i-2]
- Keep only the last two values.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def climb_stairs(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1

    a, b = 1, 1  # ways(0), ways(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    assert climb_stairs(0) == 1
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    print("ok")
