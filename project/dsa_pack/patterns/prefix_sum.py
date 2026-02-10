from __future__ import annotations

from typing import Dict, List


def build_prefix(nums: List[int]) -> List[int]:
    """Build a prefix sum array.

    prefix[0] = 0
    prefix[i+1] = sum(nums[: i+1])
    """

    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return prefix


def range_sum(prefix: List[int], left: int, right: int) -> int:
    """Sum of nums[left:right+1] given prefix where prefix[i]=sum(nums[:i])."""

    return prefix[right + 1] - prefix[left]


def count_subarrays_sum_k(nums: List[int], k: int) -> int:
    """Count subarrays with sum == k.

    Uses a hashmap of prefix-sum frequencies.

    Time: O(n)
    Space: O(n)
    """

    freq: Dict[int, int] = {0: 1}
    curr = 0
    count = 0

    for x in nums:
        curr += x
        count += freq.get(curr - k, 0)
        freq[curr] = freq.get(curr, 0) + 1

    return count
