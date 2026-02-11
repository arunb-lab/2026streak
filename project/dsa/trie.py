"""Trie (prefix tree) for lowercase words.

This structure is handy for:
- prefix queries (autocomplete)
- storing many strings with shared prefixes

This implementation supports:
- insert(word)
- contains(word)
- starts_with(prefix)
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class _Node:
    children: dict[str, "_Node"] = field(default_factory=dict)
    terminal: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = _Node()

    def insert(self, word: str) -> None:
        if word == "":
            # Allow inserting empty string; it marks root as terminal.
            self.root.terminal = True
            return

        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _Node())
        node.terminal = True

    def contains(self, word: str) -> bool:
        node = self._walk(word)
        return node.terminal if node is not None else False

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s: str) -> _Node | None:
        node = self.root
        for ch in s:
            nxt = node.children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node
