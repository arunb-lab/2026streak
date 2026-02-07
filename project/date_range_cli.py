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
from datetime import date
from pathlib import Path

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
        "--holiday",
        action="append",
        default=[],
        metavar="YYYY-MM-DD",
        help="Exclude a holiday date (repeatable)",
    )
    p.add_argument(
        "--holidays-file",
        type=Path,
        default=None,
        metavar="PATH",
        help="Path to a file with one YYYY-MM-DD per line (blank lines/# comments ok)",
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


def _parse_holidays(holiday_args: list[str], holidays_file: Path | None) -> set[date]:
    holidays: set[date] = set()

    for s in holiday_args:
        holidays.add(date.fromisoformat(s.strip()))

    if holidays_file is not None:
        for line in holidays_file.read_text(encoding="utf-8").splitlines():
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            holidays.add(date.fromisoformat(raw))

    return holidays


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    r = DateRange.from_iso(args.range).shift(days=args.shift_days)

    if args.split:
        for chunk in r.split(chunk_days=args.split):
            print(chunk.to_iso())
        return 0

    if args.business_days:
        holidays = _parse_holidays(args.holiday, args.holidays_file)
        print(r.business_days(holidays=holidays))
    else:
        print(r.days())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
