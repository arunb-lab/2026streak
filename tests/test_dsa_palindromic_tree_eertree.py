from __future__ import annotations

import random

from project.dsa.palindromic_tree_eertree import PalindromicTree


def _distinct_palindromes_bruteforce(s: str) -> int:
    pals: set[str] = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                pals.add(sub)
    return len(pals)


def test_eertree_distinct_palindromes_known() -> None:
    s = "abacaba"
    t = PalindromicTree.from_string(s)
    assert t.count_distinct_palindromes() == _distinct_palindromes_bruteforce(s)


def test_eertree_random_matches_bruteforce() -> None:
    rng = random.Random(0)
    for _ in range(100):
        n = rng.randint(0, 25)
        s = "".join(rng.choice("ab") for _ in range(n))
        t = PalindromicTree.from_string(s)
        assert t.count_distinct_palindromes() == _distinct_palindromes_bruteforce(s)
