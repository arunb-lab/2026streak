"""Aho–Corasick automaton for multi-pattern string matching.

Supports building from a list of patterns and searching all occurrences in
O(|text| + total matches) after O(sum |pattern|) build time.

This implementation assumes patterns/text are Python strings. It works with any
characters (not just lowercase).
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class _Node:
    next: dict[str, int] = field(default_factory=dict)
    link: int = 0
    out: list[int] = field(default_factory=list)  # pattern indices ending here


class AhoCorasick:
    def __init__(self, patterns: list[str]) -> None:
        if any(p is None for p in patterns):
            raise ValueError("patterns must be strings")

        self.patterns = patterns
        self.nodes: list[_Node] = [_Node()]  # root

        for i, pat in enumerate(patterns):
            self._add_pattern(pat, i)

        self._build_links()

    def _add_pattern(self, pat: str, idx: int) -> None:
        v = 0
        for ch in pat:
            nxt = self.nodes[v].next.get(ch)
            if nxt is None:
                self.nodes.append(_Node())
                nxt = len(self.nodes) - 1
                self.nodes[v].next[ch] = nxt
            v = nxt
        self.nodes[v].out.append(idx)

    def _build_links(self) -> None:
        q: deque[int] = deque()

        # root's children have link to root
        for ch, v in self.nodes[0].next.items():
            self.nodes[v].link = 0
            q.append(v)

        while q:
            v = q.popleft()
            for ch, to in self.nodes[v].next.items():
                q.append(to)

                # follow suffix links
                j = self.nodes[v].link
                while j != 0 and ch not in self.nodes[j].next:
                    j = self.nodes[j].link

                self.nodes[to].link = self.nodes[j].next.get(ch, 0)

                # inherit outputs
                self.nodes[to].out.extend(self.nodes[self.nodes[to].link].out)

    def find_all(self, text: str) -> list[tuple[int, int]]:
        """Return list of (end_index_exclusive, pattern_index) for all matches."""

        res: list[tuple[int, int]] = []
        v = 0
        for i, ch in enumerate(text):
            while v != 0 and ch not in self.nodes[v].next:
                v = self.nodes[v].link
            v = self.nodes[v].next.get(ch, 0)

            for pat_idx in self.nodes[v].out:
                res.append((i + 1, pat_idx))

        return res

    def find_spans(self, text: str) -> list[tuple[int, int, str]]:
        """Return list of (start, end_inclusive, matched_pattern) spans."""

        out: list[tuple[int, int, str]] = []
        for end_exclusive, pi in self.find_all(text):
            pat = self.patterns[pi]
            start = end_exclusive - len(pat)
            end_inclusive = end_exclusive - 1
            out.append((start, end_inclusive, pat))
        return out
