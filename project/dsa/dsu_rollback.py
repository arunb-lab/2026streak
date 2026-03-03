"""DSU (Union-Find) with rollback.

Useful for offline dynamic connectivity, divide-and-conquer on time, etc.

Operations:
- find(x)
- union(a, b) -> bool (returns True if merged)
- snapshot() -> int token
- rollback(token) -> None

All operations are (amortized) near O(alpha(n)) except rollback which is O(#ops rolled back).

Note:
- Path compression is NOT used (not rollback-friendly).
- Union by size is used.
"""

from __future__ import annotations


class DSURollback:
    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("n must be non-negative")
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
        # Stack of changes: (changed_node, old_parent, old_size_of_root, merged?)
        self._hist: list[tuple[int, int, int, bool]] = []

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            self._hist.append((0, 0, 0, False))
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        # Attach rb under ra.
        self._hist.append((rb, self.parent[rb], self.size[ra], True))
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def snapshot(self) -> int:
        return len(self._hist)

    def rollback(self, token: int) -> None:
        if token < 0 or token > len(self._hist):
            raise ValueError("invalid rollback token")
        while len(self._hist) > token:
            node, old_parent, old_size, merged = self._hist.pop()
            if not merged:
                continue
            root = self.parent[node]
            # Restore.
            self.parent[node] = old_parent
            self.size[root] = old_size
            self.components += 1
