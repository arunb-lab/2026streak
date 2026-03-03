"""Suffix Automaton (SAM).

A suffix automaton is a minimal DFA that recognizes all substrings of a string.
It can answer many advanced string queries efficiently.

This implementation supports:
- Building a SAM for a string in O(n)
- Counting distinct substrings in O(n)
- Longest common substring (LCS) length with another string in O(m)
- Occurrence counts for substrings (after a one-time propagation step)

Notes:
- States are stored in a list; transitions use dict for clarity.
- For competitive-programming speed, transitions can be replaced with arrays for
  limited alphabets.

Refs:
- E. Ukkonen (1995) / standard SAM construction.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class _State:
    """A SAM state."""

    link: int = -1
    length: int = 0
    next: dict[str, int] = field(default_factory=dict)
    # endpos size proxy: number of times this state was the last state when
    # scanning the original string (before propagation).
    occ: int = 0


class SuffixAutomaton:
    def __init__(self) -> None:
        self._st: list[_State] = [_State(link=-1, length=0)]
        self._last: int = 0
        self._built: bool = False

    @property
    def size(self) -> int:
        return len(self._st)

    def extend(self, c: str) -> None:
        """Add character c to the automaton."""

        if len(c) != 1:
            raise ValueError("extend() expects a single character")

        cur = len(self._st)
        self._st.append(_State(length=self._st[self._last].length + 1, occ=1))

        p = self._last
        while p != -1 and c not in self._st[p].next:
            self._st[p].next[c] = cur
            p = self._st[p].link

        if p == -1:
            self._st[cur].link = 0
        else:
            q = self._st[p].next[c]
            if self._st[p].length + 1 == self._st[q].length:
                self._st[cur].link = q
            else:
                clone = len(self._st)
                self._st.append(
                    _State(
                        link=self._st[q].link,
                        length=self._st[p].length + 1,
                        next=dict(self._st[q].next),
                        occ=0,
                    )
                )
                while p != -1 and self._st[p].next.get(c) == q:
                    self._st[p].next[c] = clone
                    p = self._st[p].link
                self._st[q].link = clone
                self._st[cur].link = clone

        self._last = cur
        self._built = False

    @classmethod
    def from_string(cls, s: str) -> SuffixAutomaton:
        sam = cls()
        for ch in s:
            sam.extend(ch)
        return sam

    def count_distinct_substrings(self) -> int:
        """Return the number of distinct substrings of the built string."""

        # Each state v contributes len(v) - len(link(v)) new substrings.
        total = 0
        for v in range(1, len(self._st)):
            link = self._st[v].link
            total += self._st[v].length - self._st[link].length
        return total

    def longest_common_substring_len(self, t: str) -> int:
        """Return length of the longest common substring between built s and t."""

        v = 0
        l = 0
        best = 0

        for ch in t:
            if ch in self._st[v].next:
                v = self._st[v].next[ch]
                l += 1
            else:
                while v != -1 and ch not in self._st[v].next:
                    v = self._st[v].link
                if v == -1:
                    v = 0
                    l = 0
                else:
                    l = self._st[v].length + 1
                    v = self._st[v].next[ch]
            if l > best:
                best = l

        return best

    def _propagate_occurrences(self) -> None:
        """Propagate occ counts along suffix links.

        After this, for any state v, occ(v) equals the number of occurrences
        of any substring whose path ends in v.
        """

        # Counting sort by length.
        max_len = max(st.length for st in self._st)
        bucket = [0] * (max_len + 1)
        for st in self._st:
            bucket[st.length] += 1
        for i in range(1, len(bucket)):
            bucket[i] += bucket[i - 1]

        order = [0] * len(self._st)
        for i in range(len(self._st) - 1, -1, -1):
            l = self._st[i].length
            bucket[l] -= 1
            order[bucket[l]] = i

        # Process in decreasing length.
        for v in reversed(order):
            link = self._st[v].link
            if link != -1:
                self._st[link].occ += self._st[v].occ

        self._built = True

    def occurrence_count_of(self, pattern: str) -> int:
        """Return the number of occurrences of pattern in the built string.

        This is O(|pattern|) after a one-time propagation.
        Returns 0 if pattern is not a substring.
        """

        if not self._built:
            # Safe to call multiple times.
            self._propagate_occurrences()

        v = 0
        for ch in pattern:
            nxt = self._st[v].next.get(ch)
            if nxt is None:
                return 0
            v = nxt
        return self._st[v].occ
