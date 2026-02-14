"""DSA - Arrays: Find the Duplicate Number

Problem (classic):
Given an array nums containing n+1 integers where each integer is in the range [1, n]
inclusive, there is only one repeated number. Find it without modifying the array
and using O(1) extra space.

Approach: Floyd's Tortoise and Hare (cycle detection)
Treat nums as a linked list where next(i) = nums[i]. Duplicate creates a cycle.

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def find_duplicate(nums: list[int]) -> int:
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


if __name__ == "__main__":
    assert find_duplicate([1, 3, 4, 2, 2]) == 2
    assert find_duplicate([3, 1, 3, 4, 2]) == 3
    print("ok")
