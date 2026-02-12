from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import heapq
from typing import Deque, Dict, Iterable, List, Tuple


def parse_unweighted_edges(items: Iterable[str]) -> List[Tuple[str, str]]:
    """Parse edges like "A:B" into [("A","B"), ...]."""

    out: List[Tuple[str, str]] = []
    for it in items:
        a, b = it.split(":", 1)
        out.append((a, b))
    return out


def parse_weighted_edges(items: Iterable[str]) -> List[Tuple[str, str, int]]:
    """Parse edges like "A:B:4" into [("A","B",4), ...]."""

    out: List[Tuple[str, str, int]] = []
    for it in items:
        a, b, w = it.split(":", 2)
        out.append((a, b, int(w)))
    return out


@dataclass
class BFSTraceStep:
    current: str
    queue: List[str]
    seen: List[str]


def bfs_trace(edges: List[Tuple[str, str]], start: str) -> List[BFSTraceStep]:
    """Run BFS on an undirected graph and capture step-by-step state."""

    graph: Dict[str, List[str]] = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    q: Deque[str] = deque([start])
    seen = {start}
    steps: List[BFSTraceStep] = []

    while q:
        cur = q.popleft()
        for nxt in graph.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
        steps.append(BFSTraceStep(current=cur, queue=list(q), seen=sorted(seen)))

    return steps


@dataclass
class DijkstraTraceStep:
    popped: Tuple[int, str]
    dist_snapshot: Dict[str, int]
    pq_size: int


def dijkstra_trace(
    edges: List[Tuple[str, str, int]], start: str
) -> List[DijkstraTraceStep]:
    """Run Dijkstra and capture step-by-step state (non-negative weights)."""

    graph: Dict[str, List[Tuple[str, int]]] = {}
    for a, b, w in edges:
        graph.setdefault(a, []).append((b, w))
        graph.setdefault(b, [])

    dist: Dict[str, int] = {start: 0}
    pq: List[Tuple[int, str]] = [(0, start)]

    steps: List[DijkstraTraceStep] = []

    while pq:
        d, node = heapq.heappop(pq)
        if d != dist.get(node):
            continue

        for nxt, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nxt, 10**18):
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

        steps.append(
            DijkstraTraceStep(
                popped=(d, node),
                dist_snapshot=dict(sorted(dist.items())),
                pq_size=len(pq),
            )
        )

    return steps
