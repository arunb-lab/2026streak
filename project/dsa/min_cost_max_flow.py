"""Min-Cost Max-Flow (successive shortest augmenting paths + potentials).

Computes a min-cost flow of maximum value (or up to a desired flow) in a
capacitated directed graph.

- Supports negative edge costs as long as there are no negative cycles
  reachable from the source in the residual graph.
- Uses Johnson-style potentials to run Dijkstra on reduced costs.

Complexity:
- O(F * E log V) for integral capacities where F is total flow sent.

Refs:
- Successive shortest augmenting path algorithm
- Potentials / reduced costs (Johnson)
"""

from __future__ import annotations

from dataclasses import dataclass
import heapq


@dataclass
class _Edge:
    to: int
    rev: int
    cap: int
    cost: int


class MinCostMaxFlow:
    def __init__(self, n: int) -> None:
        if n <= 0:
            raise ValueError("n must be positive")
        self.n = n
        self.g: list[list[_Edge]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int, cost: int) -> None:
        """Add directed edge u->v with capacity cap and per-unit cost."""

        if cap < 0:
            raise ValueError("cap must be non-negative")
        if not (0 <= u < self.n and 0 <= v < self.n):
            raise IndexError("node out of range")
        fwd = _Edge(to=v, rev=len(self.g[v]), cap=int(cap), cost=int(cost))
        rev = _Edge(to=u, rev=len(self.g[u]), cap=0, cost=-int(cost))
        self.g[u].append(fwd)
        self.g[v].append(rev)

    def min_cost_flow(self, s: int, t: int, max_flow: int | None = None) -> tuple[int, int]:
        """Return (flow, cost) for min-cost flow from s to t.

        If max_flow is None, sends as much as possible (max flow).
        """

        if not (0 <= s < self.n and 0 <= t < self.n):
            raise IndexError("node out of range")
        if s == t:
            return (0, 0)

        flow = 0
        cost = 0
        inf = 10**30

        # Potential for reduced costs; starts at 0.
        pot = [0] * self.n

        parent_v = [-1] * self.n
        parent_e = [-1] * self.n

        while max_flow is None or flow < max_flow:
            dist = [inf] * self.n
            dist[s] = 0
            pq: list[tuple[int, int]] = [(0, s)]

            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for ei, e in enumerate(self.g[u]):
                    if e.cap <= 0:
                        continue
                    nd = d + e.cost + pot[u] - pot[e.to]
                    if nd < dist[e.to]:
                        dist[e.to] = nd
                        parent_v[e.to] = u
                        parent_e[e.to] = ei
                        heapq.heappush(pq, (nd, e.to))

            if dist[t] == inf:
                break

            # Update potentials.
            for v in range(self.n):
                if dist[v] < inf:
                    pot[v] += dist[v]

            # Find augmenting amount.
            add = inf
            v = t
            while v != s:
                u = parent_v[v]
                ei = parent_e[v]
                if u == -1 or ei == -1:
                    raise RuntimeError("internal error: missing parent")
                e = self.g[u][ei]
                add = min(add, e.cap)
                v = u

            if max_flow is not None:
                add = min(add, max_flow - flow)

            # Apply augmentation.
            v = t
            while v != s:
                u = parent_v[v]
                ei = parent_e[v]
                e = self.g[u][ei]
                e.cap -= add
                self.g[v][e.rev].cap += add
                cost += add * e.cost
                v = u

            flow += add

        return (flow, cost)


def min_cost_max_flow(
    n: int, edges: list[tuple[int, int, int, int]], s: int, t: int, max_flow: int | None = None
) -> tuple[int, int]:
    """Convenience wrapper."""

    m = MinCostMaxFlow(n)
    for u, v, cap, c in edges:
        m.add_edge(u, v, cap, c)
    return m.min_cost_flow(s, t, max_flow=max_flow)
