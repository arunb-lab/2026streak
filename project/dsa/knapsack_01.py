"""0/1 Knapsack (dynamic programming).

Given items with (weight, value) and a capacity W, pick a subset (each item at most
once) to maximize total value.

This module provides:
- knapsack_01_max_value: returns best achievable value

Time:  O(n * W)
Space: O(W)
"""

from __future__ import annotations


def knapsack_01_max_value(
    weights: list[int], values: list[int], capacity: int
) -> int:
    if capacity < 0:
        raise ValueError("capacity must be >= 0")
    if len(weights) != len(values):
        raise ValueError("weights and values must have same length")

    dp = [0] * (capacity + 1)

    for w, val in zip(weights, values, strict=True):
        if w < 0:
            raise ValueError("weights must be >= 0")
        # reverse to avoid reusing the same item multiple times
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + val)

    return dp[capacity]
