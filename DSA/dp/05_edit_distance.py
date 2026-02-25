"""DSA - DP: Edit Distance (Levenshtein)

Problem:
Given strings word1 and word2, return the minimum number of operations required
to convert word1 to word2. Allowed operations:
- insert a character
- delete a character
- replace a character

DP definition:
Let dp[i][j] be the edit distance between word1[:i] and word2[:j].
Transition:
- if last chars equal: dp[i][j] = dp[i-1][j-1]
- else: 1 + min(replace, delete, insert)

Optimization:
Use 2 rows to reduce space.

Time: O(m*n)
Space: O(n)
"""

from __future__ import annotations


def edit_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j - 1],  # replace
                    prev[j],      # delete
                    curr[j - 1],  # insert
                )
        prev = curr

    return prev[n]


if __name__ == "__main__":
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3
    assert edit_distance("abc", "abc") == 0
    print("ok")
