"""DSA - DP: Coin Change

Problem:
Given coins of different denominations and an integer amount, return the fewest
number of coins that you need to make up that amount. If that amount cannot be
made up, return -1.

Approach (bottom-up DP):
- dp[a] = minimum coins to make amount a
- dp[0] = 0; dp[a] = 1 + min(dp[a - c]) for all coins c <= a

Time: O(amount * len(coins))
Space: O(amount)
"""

from __future__ import annotations


def coin_change(coins: list[int], amount: int) -> int:
    if amount < 0:
        return -1
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        best = INF
        for c in coins:
            if c <= a:
                best = min(best, dp[a - c] + 1)
        dp[a] = best

    return -1 if dp[amount] >= INF else dp[amount]


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3  # 5+5+1
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 2) == 2
    print("ok")
