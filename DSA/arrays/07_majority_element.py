"""DSA - Arrays: Majority Element

Problem:
Find the element that appears more than ⌊n/2⌋ times.

Approach: Boyer–Moore majority vote algorithm
- Keep a candidate and a counter
- When counter hits 0, pick new candidate
- Increment if same, decrement if different

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def majority_element(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")

    candidate = nums[0]
    count = 1
    for x in nums[1:]:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    return candidate


if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    print("ok")
