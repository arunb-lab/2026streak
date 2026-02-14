"""DSA - Arrays: Best Time to Buy and Sell Stock

Problem:
Given prices where prices[i] is the price on day i, maximize profit by choosing
one day to buy and a later day to sell. Return max profit (0 if none).

Approach:
- Track minimum price so far
- Update best profit at each step

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def max_profit(prices: list[int]) -> int:
    min_price = 10**18
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print("ok")
