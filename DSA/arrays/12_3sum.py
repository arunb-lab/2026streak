"""DSA - Arrays: 3Sum

Problem:
Given an integer array nums, return all unique triplets [a,b,c] such that:
- a + b + c == 0
- indices are distinct
- the set of triplets contains no duplicates

Approach (sort + two pointers):
- Sort nums.
- Fix i, then solve 2-sum on the suffix with l/r pointers.
- Skip duplicates for i, l, r.

Time: O(n^2)
Space: O(1) extra (output excluded)
"""

from __future__ import annotations


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # If the smallest possible sum is already > 0, no solutions further.
        if nums[i] > 0:
            break

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

    return res


if __name__ == "__main__":
    out = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted(out) == sorted([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, -2, -1]) == []
    print("ok")
