"""Small CLI for DateRange.

Examples:
  python -m project.date_range_cli 2026-01-01..2026-01-31
  python -m project.date_range_cli 2026-01-01..2026-01-31 --business-days
  python -m project.date_range_cli 2026-01-01..2026-01-31 --split 7
  python -m project.date_range_cli 2026-01-01..2026-01-31 --shift-days 1

This is intentionally minimal, but demonstrates argparse + tested core logic.
"""

from __future__ import annotations

import argparse

from project.date_range import DateRange


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Work with a YYYY-MM-DD..YYYY-MM-DD range")
    p.add_argument("range", help="Date range in ISO form: YYYY-MM-DD..YYYY-MM-DD")

    p.add_argument(
        "--business-days",
        action="store_true",
        help="Count only weekdays (Mon–Fri)",
    )
    p.add_argument(
        "--shift-days",
        type=int,
        default=0,
        help="Shift the range by N days before computing output",
    )
    p.add_argument(
        "--split",
        type=int,
        default=0,
        metavar="N",
        help="Split the range into chunks of N days and print each chunk",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    r = DateRange.from_iso(args.range).shift(days=args.shift_days)

    if args.split:
        for chunk in r.split(chunk_days=args.split):
            print(chunk.to_iso())
        return 0

    if args.business_days:
        print(r.business_days())
    else:
        print(r.days())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
