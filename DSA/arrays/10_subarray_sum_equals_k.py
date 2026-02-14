"""DSA - Arrays: Subarray Sum Equals K

Problem:
Given an integer array nums and an integer k, return the total number of
continuous subarrays whose sum equals k.

Approach: prefix sums + hashmap counts
Let prefix[i] = sum(nums[:i]). Subarray (l..r] sums to k when
prefix[r] - prefix[l] = k  => prefix[l] = prefix[r] - k.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    freq: dict[int, int] = {0: 1}

    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3
    print("ok")
