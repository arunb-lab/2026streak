"""Small CLI for DateRange.

Examples:
  python -m project.date_range_cli 2026-01-01..2026-01-31
  python -m project.date_range_cli 2026-01-01..2026-01-31 --business-days

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
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    r = DateRange.from_iso(args.range)

    if args.business_days:
        print(r.business_days())
    else:
        print(r.days())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
