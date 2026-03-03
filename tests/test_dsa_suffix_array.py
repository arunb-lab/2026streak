from __future__ import annotations

import random

from project.dsa.suffix_array import lcp_array, suffix_array


def test_suffix_array_banana() -> None:
    s = "banana"
    sa = suffix_array(s)
    assert sa == sorted(range(len(s)), key=lambda i: s[i:])

    lcp = lcp_array(s, sa)
    # Basic sanity: lcp[0]=0 and each lcp <= remaining length.
    assert lcp[0] == 0
    for r, i in enumerate(sa):
        assert 0 <= lcp[r] <= len(s) - i


def test_suffix_array_random_matches_bruteforce() -> None:
    rng = random.Random(0)
    for _ in range(100):
        n = rng.randint(0, 30)
        s = "".join(rng.choice("abca") for _ in range(n))
        sa = suffix_array(s)
        assert sa == sorted(range(len(s)), key=lambda i: s[i:])
        if s:
            lcp = lcp_array(s, sa)
            # Verify LCP definition.
            for r in range(1, len(sa)):
                i, j = sa[r], sa[r - 1]
                k = 0
                while i + k < len(s) and j + k < len(s) and s[i + k] == s[j + k]:
                    k += 1
                assert lcp[r] == k
