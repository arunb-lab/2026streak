"""LRU Cache (Least Recently Used).

A fixed-capacity cache supporting O(1) average:
- get(key)
- put(key, value)

Implementation uses collections.OrderedDict:
- move_to_end marks most-recently-used
- popitem(last=False) evicts least-recently-used

This is a common interview data structure because it combines:
- hash map
- doubly-linked list ordering
"""

from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass(frozen=True)
class CacheStats:
    hits: int
    misses: int
    evictions: int


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be >= 1")
        self._cap = capacity
        self._od: OrderedDict[K, V] = OrderedDict()
        self._hits = 0
        self._misses = 0
        self._evictions = 0

    @property
    def capacity(self) -> int:
        return self._cap

    def __len__(self) -> int:
        return len(self._od)

    def stats(self) -> CacheStats:
        return CacheStats(self._hits, self._misses, self._evictions)

    def get(self, key: K) -> V | None:
        if key not in self._od:
            self._misses += 1
            return None
        self._hits += 1
        self._od.move_to_end(key)
        return self._od[key]

    def put(self, key: K, value: V) -> None:
        if key in self._od:
            self._od[key] = value
            self._od.move_to_end(key)
            return

        self._od[key] = value
        self._od.move_to_end(key)

        if len(self._od) > self._cap:
            self._od.popitem(last=False)
            self._evictions += 1

    def keys_mru_to_lru(self) -> list[K]:
        """Inspect ordering for debugging/tests."""

        return list(reversed(self._od.keys()))
