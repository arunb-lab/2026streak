"""Educational hash table with separate chaining.

This is NOT meant to compete with Python's dict; it's for learning.

Key points:
- bucketed storage (list of lists)
- resizing when load factor grows
- expected O(1) operations under uniform hashing

Limitations:
- Uses Python's built-in `hash()`; real hash tables include more optimizations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, List, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Entry(Generic[K, V]):
    key: K
    value: V


class HashTable(Generic[K, V]):
    def __init__(self, initial_capacity: int = 8, max_load: float = 0.75) -> None:
        if initial_capacity <= 0 or (initial_capacity & (initial_capacity - 1)) != 0:
            raise ValueError("initial_capacity must be a power of two")
        self._buckets: List[List[_Entry[K, V]]] = [[] for _ in range(initial_capacity)]
        self._size = 0
        self._max_load = max_load

    def __len__(self) -> int:
        return self._size

    def _index(self, key: K) -> int:
        return hash(key) & (len(self._buckets) - 1)

    def _maybe_resize(self) -> None:
        if self._size / len(self._buckets) <= self._max_load:
            return
        old = self._buckets
        self._buckets = [[] for _ in range(len(old) * 2)]
        self._size = 0
        for bucket in old:
            for e in bucket:
                self[e.key] = e.value

    def __setitem__(self, key: K, value: V) -> None:
        self._maybe_resize()
        idx = self._index(key)
        bucket = self._buckets[idx]
        for e in bucket:
            if e.key == key:
                e.value = value
                return
        bucket.append(_Entry(key, value))
        self._size += 1

    def __getitem__(self, key: K) -> V:
        idx = self._index(key)
        for e in self._buckets[idx]:
            if e.key == key:
                return e.value
        raise KeyError(key)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key: K) -> None:
        idx = self._index(key)
        bucket = self._buckets[idx]
        for i, e in enumerate(bucket):
            if e.key == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def items(self) -> Iterator[Tuple[K, V]]:
        for bucket in self._buckets:
            for e in bucket:
                yield (e.key, e.value)


def _demo() -> None:
    ht: HashTable[str, int] = HashTable()
    ht["a"] = 1
    ht["b"] = 2
    ht["a"] = 3
    print("size", len(ht))
    print("a", ht["a"])
    print("items", sorted(ht.items()))


if __name__ == "__main__":
    _demo()
