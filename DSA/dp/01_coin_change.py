"""DSA - Dynamic Programming: Coin Change (minimum coins)

Problem:
Given coins (distinct positive integers) and an amount, return the fewest number
of coins needed to make up that amount. If impossible, return -1.

Classic 1D DP:
- dp[x] = minimum coins to make sum x
- dp[0] = 0
- dp[x] = min(dp[x - c] + 1 for c in coins if x - c >= 0)

Time: O(amount * len(coins))
Space: O(amount)
"""

from __future__ import annotations

import math


def coin_change_min_coins(coins: list[int], amount: int) -> int:
    if amount < 0:
        raise ValueError("amount must be >= 0")
    if any(c <= 0 for c in coins):
        raise ValueError("all coins must be positive")

    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for x in range(1, amount + 1):
        best = math.inf
        for c in coins:
            if x - c >= 0 and dp[x - c] != math.inf:
                best = min(best, dp[x - c] + 1)
        dp[x] = best

    return -1 if dp[amount] == math.inf else int(dp[amount])


if __name__ == "__main__":
    assert coin_change_min_coins([1, 2, 5], 11) == 3  # 5+5+1
    assert coin_change_min_coins([2], 3) == -1
    assert coin_change_min_coins([1], 0) == 0
    assert coin_change_min_coins([2, 5, 10, 1], 27) == 4  # 10+10+5+2
    print("ok")
