"""Coin change (minimum coins).

Given coin denominations and a target amount, compute the minimum number of coins
needed to make exactly that amount.

- coin_change_min_coins(coins, amount) -> int | None

Returns None if it's not possible.

Time:  O(amount * len(coins))
Space: O(amount)
"""

from __future__ import annotations

from math import inf


def coin_change_min_coins(coins: list[int], amount: int) -> int | None:
    if amount < 0:
        raise ValueError("amount must be >= 0")
    if amount == 0:
        return 0
    if any(c <= 0 for c in coins):
        raise ValueError("coin values must be positive")

    dp = [inf] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        best = inf
        for c in coins:
            if a - c >= 0:
                best = min(best, dp[a - c] + 1)
        dp[a] = best

    return None if dp[amount] == inf else int(dp[amount])
