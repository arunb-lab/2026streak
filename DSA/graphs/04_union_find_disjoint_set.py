"""DSA - Graphs: Union-Find (Disjoint Set Union)

Use-cases:
- Detect cycle in undirected graph
- Count connected components
- Kruskal's MST

Optimizations:
- Path compression in find
- Union by size

Amortized time per operation: ~O(alpha(n)) (inverse Ackermann)
Space: O(n)
"""

from __future__ import annotations


class UnionFind:
    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("n must be non-negative")
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.components == 5
    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.union(0, 2) is False
    assert uf.find(2) == uf.find(0)
    assert uf.components == 3
    print("ok")
