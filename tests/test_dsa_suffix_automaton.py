from __future__ import annotations

import random

from project.dsa.suffix_automaton import SuffixAutomaton


def _distinct_substrings_bruteforce(s: str) -> int:
    subs: set[str] = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs.add(s[i:j])
    return len(subs)


def test_count_distinct_substrings_known() -> None:
    sam = SuffixAutomaton.from_string("ababa")
    assert sam.count_distinct_substrings() == _distinct_substrings_bruteforce("ababa")


def test_lcs_len() -> None:
    sam = SuffixAutomaton.from_string("banana")
    assert sam.longest_common_substring_len("ananas") == 5  # "anana"
    assert sam.longest_common_substring_len("xyz") == 0


def test_occurrence_counts() -> None:
    sam = SuffixAutomaton.from_string("aaaa")
    assert sam.occurrence_count_of("a") == 4
    assert sam.occurrence_count_of("aa") == 3
    assert sam.occurrence_count_of("aaa") == 2
    assert sam.occurrence_count_of("aaaa") == 1
    assert sam.occurrence_count_of("b") == 0


def test_random_distinct_substrings_matches_bruteforce() -> None:
    rng = random.Random(0)
    for _ in range(50):
        n = rng.randint(0, 8)
        s = "".join(rng.choice("abc") for _ in range(n))
        sam = SuffixAutomaton.from_string(s)
        assert sam.count_distinct_substrings() == _distinct_substrings_bruteforce(s)
