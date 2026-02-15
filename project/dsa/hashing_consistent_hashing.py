from __future__ import annotations

import hashlib
from bisect import bisect_left


def _h64(data: bytes) -> int:
    """Stable 64-bit hash using SHA-256 (take first 8 bytes).

    We avoid Python's built-in hash() here because it's salted per-process.
    """

    digest = hashlib.sha256(data).digest()
    return int.from_bytes(digest[:8], byteorder="big", signed=False)


class ConsistentHashRing:
    """A simple consistent hashing ring with virtual nodes.

    Typical use: distribute keys across a changing set of nodes.

    Properties:
    - When adding/removing a node, only ~1/N keys move.
    - Virtual nodes improve balance.

    This is an educational implementation; production systems need more
    observability and careful tuning.
    """

    def __init__(self, replicas: int = 64) -> None:
        if replicas <= 0:
            raise ValueError("replicas must be > 0")
        self._replicas = replicas
        self._points: list[int] = []
        self._owners: list[str] = []
        self._nodes: set[str] = set()

    @property
    def nodes(self) -> set[str]:
        return set(self._nodes)

    def add_node(self, node_id: str) -> None:
        if node_id in self._nodes:
            return

        self._nodes.add(node_id)
        for r in range(self._replicas):
            p = _h64(f"{node_id}#{r}".encode("utf-8"))
            i = bisect_left(self._points, p)
            self._points.insert(i, p)
            self._owners.insert(i, node_id)

    def remove_node(self, node_id: str) -> None:
        if node_id not in self._nodes:
            return
        self._nodes.remove(node_id)

        # Filter out virtual nodes belonging to node_id.
        new_points: list[int] = []
        new_owners: list[str] = []
        for p, o in zip(self._points, self._owners, strict=True):
            if o != node_id:
                new_points.append(p)
                new_owners.append(o)

        self._points = new_points
        self._owners = new_owners

    def get_node(self, key: str) -> str | None:
        """Return the node that owns this key, or None if ring is empty."""
        if not self._points:
            return None

        p = _h64(key.encode("utf-8"))
        i = bisect_left(self._points, p)
        if i == len(self._points):
            i = 0
        return self._owners[i]
