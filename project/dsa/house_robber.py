"""House Robber (LeetCode 198).

Problem:
You are given an integer array `nums` where `nums[i]` is the amount of money in
the i-th house. You cannot rob two adjacent houses.

Return the maximum amount of money you can rob.

Approach (DP, rolling):
Let dp[i] be the best we can do considering houses up to i.
Transition: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
We keep only the last two values.

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations


def house_robber(nums: list[int]) -> int:
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for x in nums:
        if x < 0:
            raise ValueError("nums must be non-negative")
        cur = max(prev1, prev2 + x)
        prev2, prev1 = prev1, cur

    return prev1
