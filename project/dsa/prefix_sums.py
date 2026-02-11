"""Prefix sums & hash-map counting.

Prefix sums let you answer range-sum queries in O(1) after O(n) preprocessing.
A common trick: count subarrays with sum == k by tracking counts of seen prefixes.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PrefixSums:
    """Immutable prefix sums helper for integer arrays."""

    prefix: list[int]

    @classmethod
    def from_list(cls, nums: list[int]) -> "PrefixSums":
        p = [0]
        s = 0
        for x in nums:
            s += x
            p.append(s)
        return cls(prefix=p)

    def range_sum(self, left: int, right_exclusive: int) -> int:
        """Sum(nums[left:right_exclusive])."""

        if left < 0 or right_exclusive < left or right_exclusive >= len(self.prefix):
            raise ValueError("invalid range")
        return self.prefix[right_exclusive] - self.prefix[left]


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """Count subarrays with sum exactly k.

    Works with negative numbers.

    Time:  O(n)
    Space: O(n)
    """

    count = 0
    prefix = 0
    seen: dict[int, int] = {0: 1}

    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count
