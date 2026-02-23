"""DSA - DP: House Robber

Problem:
You are a professional robber planning to rob houses along a street.
Adjacent houses have security systems connected; you cannot rob adjacent houses.
Return the maximum amount of money you can rob.

Approach (rolling DP):
Let dp[i] be max money from first i houses.
Transition: dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
We keep only two variables.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def rob(nums: list[int]) -> int:
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for x in nums:
        cur = max(prev1, prev2 + x)
        prev2, prev1 = prev1, cur

    return prev1


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
    print("ok")
