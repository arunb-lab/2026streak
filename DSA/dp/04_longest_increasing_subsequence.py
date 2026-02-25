"""DSA - DP: Longest Increasing Subsequence (LIS)

Problem:
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Approach (patience sorting / tails):
- Maintain tails[k] = minimum possible tail value of an increasing subsequence
  of length k+1.
- For each x, binary-search the first index i with tails[i] >= x and replace.

Time: O(n log n)
Space: O(n)
"""

from __future__ import annotations

import bisect


def lis_length(nums: list[int]) -> int:
    tails: list[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


if __name__ == "__main__":
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([0, 1, 0, 3, 2, 3]) == 4
    assert lis_length([7, 7, 7, 7]) == 1
    assert lis_length([]) == 0
    print("ok")
