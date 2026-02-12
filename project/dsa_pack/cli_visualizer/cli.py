from __future__ import annotations

import argparse
import json
from typing import List

from project.dsa_pack.cli_visualizer.traces import (
    bfs_trace,
    dijkstra_trace,
    parse_unweighted_edges,
    parse_weighted_edges,
)


def _cmd_bfs(args: argparse.Namespace) -> int:
    edges = parse_unweighted_edges(args.edges)
    steps = bfs_trace(edges=edges, start=args.start)

    if args.json:
        print(json.dumps([s.__dict__ for s in steps], indent=2))
        return 0

    for i, s in enumerate(steps, start=1):
        print(f"step {i:02d} | current={s.current} | queue={s.queue} | seen={s.seen}")

    return 0


def _cmd_dijkstra(args: argparse.Namespace) -> int:
    edges = parse_weighted_edges(args.edges)
    steps = dijkstra_trace(edges=edges, start=args.start)

    if args.json:
        print(
            json.dumps(
                [
                    {"popped": s.popped, "dist": s.dist_snapshot, "pq_size": s.pq_size}
                    for s in steps
                ],
                indent=2,
            )
        )
        return 0

    for i, s in enumerate(steps, start=1):
        d, node = s.popped
        print(
            f"step {i:02d} | popped=({d},{node}) | pq_size={s.pq_size} "
            f"| dist={s.dist_snapshot}"
        )

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="dsa-visualizer", description="Trace BFS / Dijkstra step-by-step"
    )
    p.add_argument("--json", action="store_true", help="output trace as JSON")

    sub = p.add_subparsers(dest="cmd", required=True)

    bfs = sub.add_parser("bfs", help="trace BFS on an undirected graph")
    bfs.add_argument("--start", required=True)
    bfs.add_argument(
        "--edges",
        nargs="*",
        default=[],
        help='Edges like "A:B" (space-separated). Example: --edges A:B A:C B:D',
    )
    bfs.set_defaults(func=_cmd_bfs)

    dij = sub.add_parser("dijkstra", help="trace Dijkstra on a directed weighted graph")
    dij.add_argument("--start", required=True)
    dij.add_argument(
        "--edges",
        nargs="*",
        default=[],
        help='Edges like "A:B:4" (space-separated). Example: --edges A:B:4 A:C:2 C:B:1',
    )
    dij.set_defaults(func=_cmd_dijkstra)

    return p


def main(argv: List[str] | None = None) -> int:
    p = build_parser()
    args = p.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
