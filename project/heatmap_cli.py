"""CLI for generating a GitHub-like contribution heatmap SVG.

Input format (JSON):
A mapping of ISO date string -> integer count.

Example counts.json:
{
  "2026-01-01": 3,
  "2026-01-02": 0,
  "2026-01-03": 7
}

Usage:
  python -m project.heatmap_cli --counts counts.json --start 2026-01-01 --end 2026-12-31
  python -m project.heatmap_cli --counts counts.json --last-days 365 --out heatmap.svg
"""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path

from project.heatmap import build_heatmap
from project.heatmap_svg import render_svg


def _load_counts(path: Path) -> dict[date, int]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("counts JSON must be an object mapping date->count")

    out: dict[date, int] = {}
    for k, v in raw.items():
        d = date.fromisoformat(str(k))
        out[d] = int(v)
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate a contribution heatmap SVG")
    p.add_argument("--counts", type=Path, required=True, help="Path to counts.json")

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--last-days",
        type=int,
        metavar="N",
        help="Build heatmap for last N days",
    )
    g.add_argument("--start", type=date.fromisoformat, help="Start date (YYYY-MM-DD)")

    p.add_argument(
        "--end",
        type=date.fromisoformat,
        default=None,
        help="End date (YYYY-MM-DD). Required when using --start.",
    )

    p.add_argument("--out", type=Path, default=None, help="Write SVG to this path")
    p.add_argument("--title", type=str, default="", help="Optional SVG title")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    counts = _load_counts(args.counts)

    if args.last_days is not None:
        if args.last_days <= 0:
            raise SystemExit("--last-days must be > 0")
        end = date.today()
        start = end - timedelta(days=args.last_days - 1)
    else:
        start = args.start
        if args.end is None:
            raise SystemExit("--end is required when using --start")
        end = args.end

    h = build_heatmap(start, end, counts)
    svg = render_svg(h, title=args.title)

    if args.out is None:
        print(svg, end="")
    else:
        args.out.write_text(svg, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
