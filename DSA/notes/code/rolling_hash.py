"""Polynomial rolling hash for strings.

This demonstrates:
- prefix hashing
- O(1) substring hash queries

Used in algorithms like Rabin–Karp.

Note: Python's built-in hashing is not stable across runs (hash randomization).
For algorithmic rolling hashes, we control the modulus/base ourselves.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RollingHash:
    s: str
    base: int = 911382323
    mod: int = 1_000_000_007

    def __post_init__(self) -> None:
        n = len(self.s)
        pref = [0] * (n + 1)
        pows = [1] * (n + 1)

        for i, ch in enumerate(self.s):
            x = ord(ch)
            pref[i + 1] = (pref[i] * self.base + x) % self.mod
            pows[i + 1] = (pows[i] * self.base) % self.mod

        object.__setattr__(self, "_pref", pref)
        object.__setattr__(self, "_pows", pows)

    def hash_substring(self, l: int, r: int) -> int:
        """Hash of s[l:r] (half-open interval)."""
        pref = self._pref
        pows = self._pows
        return (pref[r] - pref[l] * pows[r - l]) % self.mod


def find_occurrences(text: str, pattern: str) -> list[int]:
    """Rabin–Karp style search with verification."""
    if pattern == "":
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []

    ht = RollingHash(text)
    hp = RollingHash(pattern)
    target = hp.hash_substring(0, len(pattern))

    out: list[int] = []
    m = len(pattern)

    for i in range(0, len(text) - m + 1):
        if ht.hash_substring(i, i + m) == target:
            # verify to avoid collision false positives
            if text[i : i + m] == pattern:
                out.append(i)

    return out


def _demo() -> None:
    t = "ababcabcababc"
    p = "abc"
    print(find_occurrences(t, p))


if __name__ == "__main__":
    _demo()
