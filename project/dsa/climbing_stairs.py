"""Climbing stairs.

Problem:
You are climbing a staircase with n steps.
Each time you can climb either 1 or 2 steps.
How many distinct ways can you climb to the top?

This is Fibonacci-like.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def climbing_stairs(n: int) -> int:
    """Return number of distinct ways to climb n steps.

    Convention:
    - n = 0 -> 1 way (do nothing)

    Raises:
        ValueError: if n < 0.
    """

    if n < 0:
        raise ValueError("n must be >= 0")

    a, b = 1, 1  # ways(0), ways(1)
    for _ in range(n):
        a, b = b, a + b
    return a
