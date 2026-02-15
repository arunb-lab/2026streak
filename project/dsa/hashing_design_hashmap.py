from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Entry(Generic[K, V]):
    key: K
    value: V


class HashMap(Generic[K, V]):
    """A tiny educational HashMap using separate chaining.

    Notes:
    - This is NOT meant to beat Python's built-in dict.
    - It's here to show the core mechanics: hashing, buckets, collisions,
      resizing, and basic operations.

    Operations are O(1) expected, O(n) worst-case.
    """

    def __init__(self, initial_capacity: int = 8, load_factor: float = 0.75) -> None:
        if initial_capacity <= 0:
            raise ValueError("initial_capacity must be > 0")
        if not (0.1 <= load_factor <= 0.95):
            raise ValueError("load_factor must be in [0.1, 0.95]")

        cap = 1
        while cap < initial_capacity:
            cap <<= 1

        self._buckets: list[list[_Entry[K, V]]] = [[] for _ in range(cap)]
        self._size = 0
        self._max_load = load_factor

    def __len__(self) -> int:
        return self._size

    def _bucket_index(self, key: K) -> int:
        # bucket count is power of two, so bitmask works
        return hash(key) & (len(self._buckets) - 1)

    def _maybe_resize(self) -> None:
        if self._size / len(self._buckets) <= self._max_load:
            return

        old = self._buckets
        self._buckets = [[] for _ in range(len(old) * 2)]
        self._size = 0

        for bucket in old:
            for e in bucket:
                self.put(e.key, e.value)

    def put(self, key: K, value: V) -> None:
        """Insert or update key."""
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]

        for e in bucket:
            if e.key == key:
                e.value = value
                return

        bucket.append(_Entry(key, value))
        self._size += 1
        self._maybe_resize()

    def get(self, key: K, default: V | None = None) -> V | None:
        """Return value if key exists, else default (None by default)."""
        idx = self._bucket_index(key)
        for e in self._buckets[idx]:
            if e.key == key:
                return e.value
        return default

    def remove(self, key: K) -> bool:
        """Remove key if present. Returns True if removed."""
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]

        for i, e in enumerate(bucket):
            if e.key == key:
                bucket.pop(i)
                self._size -= 1
                return True

        return False
