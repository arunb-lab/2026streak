"""DSA - Strings: Group Anagrams

Problem:
Given an array of strings, group the anagrams together.

Approach:
Use a hashmap keyed by the 26-letter frequency signature.
For lowercase English letters: signature is a 26-tuple of counts.

Time: O(total_characters)
Space: O(n)
"""

from __future__ import annotations

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

    for s in strs:
        freq = [0] * 26
        for ch in s:
            idx = ord(ch) - ord("a")
            if idx < 0 or idx >= 26:
                raise ValueError("only lowercase a-z supported")
            freq[idx] += 1
        groups[tuple(freq)].append(s)

    return list(groups.values())


if __name__ == "__main__":
    out = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    out_sorted = sorted([sorted(g) for g in out])
    assert out_sorted == sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    print("ok")
