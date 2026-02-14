"""DSA - Arrays: Move Zeroes

Problem:
Move all 0s to the end while maintaining relative order of non-zero elements.

Two-pointer compaction:
- write points to next position for a non-zero
- first pass write non-zeros
- second pass fill the rest with zeros

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def move_zeroes(nums: list[int]) -> None:
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    assert a == [1, 3, 12, 0, 0]
    b = [0]
    move_zeroes(b)
    assert b == [0]
    print("ok")
