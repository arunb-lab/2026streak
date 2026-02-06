"""Date range utilities.

Why this exists:
- Lots of real-world backend tasks involve working with date intervals: billing
  cycles, reporting windows, subscriptions, availability, etc.
- This module aims to be *small but solid*: typed, tested, and explicit about
  inclusive/exclusive boundaries.

The core type is :class:`DateRange`, representing a range of calendar dates.

Design choices:
- The default is **inclusive** of the end date (common in reporting windows).
- For exclusive end semantics, set ``inclusive_end=False``.

Python: 3.10+
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterable, Iterator, Optional


_ISO_RANGE_SEP = ".."


@dataclass(frozen=True, slots=True)
class DateRange:
    """A range of dates with configurable end boundary.

    Args:
        start: Start date.
        end: End date.
        inclusive_end: If True, the end date is included in the range.
            If False, the range is half-open [start, end).

    Raises:
        ValueError: If ``start`` is after ``end`` (or equal when exclusive).
    """

    start: date
    end: date
    inclusive_end: bool = True

    def __post_init__(self) -> None:
        if self.inclusive_end:
            if self.start > self.end:
                raise ValueError("start must be <= end for inclusive ranges")
        else:
            if self.start >= self.end:
                raise ValueError("start must be < end for exclusive ranges")

    @property
    def end_exclusive(self) -> date:
        """Return the exclusive end date.

        For inclusive ranges, this is ``end + 1 day``.
        For exclusive ranges, this is just ``end``.
        """

        return self.end + timedelta(days=1) if self.inclusive_end else self.end

    def days(self) -> int:
        """Number of dates in the range."""

        return (self.end_exclusive - self.start).days

    def contains(self, d: date) -> bool:
        """Return True if *d* is inside the range."""

        return self.start <= d < self.end_exclusive

    def iter_days(self) -> Iterator[date]:
        """Iterate every date in the range."""

        cur = self.start
        end_excl = self.end_exclusive
        while cur < end_excl:
            yield cur
            cur += timedelta(days=1)

    def business_days(self) -> int:
        """Count Mon–Fri days in the range."""

        return sum(1 for d in self.iter_days() if d.weekday() < 5)

    def overlaps(self, other: "DateRange") -> bool:
        """Return True if two ranges share at least one date."""

        return self.start < other.end_exclusive and other.start < self.end_exclusive

    def intersection(self, other: "DateRange") -> Optional["DateRange"]:
        """Return the overlapping range, or None if there is no overlap."""

        start = max(self.start, other.start)
        end_excl = min(self.end_exclusive, other.end_exclusive)
        if start >= end_excl:
            return None
        end_inclusive = end_excl - timedelta(days=1)
        return DateRange(start=start, end=end_inclusive, inclusive_end=True)

    def to_iso(self) -> str:
        """Serialize as ``YYYY-MM-DD..YYYY-MM-DD`` (inclusive end)."""

        if not self.inclusive_end:
            end_inclusive = self.end - timedelta(days=1)
            return (
                f"{self.start.isoformat()}{_ISO_RANGE_SEP}{end_inclusive.isoformat()}"
            )
        return f"{self.start.isoformat()}{_ISO_RANGE_SEP}{self.end.isoformat()}"

    @classmethod
    def from_iso(cls, s: str) -> "DateRange":
        """Parse ``YYYY-MM-DD..YYYY-MM-DD`` into an inclusive range."""

        try:
            start_s, end_s = s.split(_ISO_RANGE_SEP, 1)
            start = date.fromisoformat(start_s.strip())
            end = date.fromisoformat(end_s.strip())
        except Exception as e:
            raise ValueError(
                f"Invalid date range '{s}'. Expected 'YYYY-MM-DD..YYYY-MM-DD'."
            ) from e
        return cls(start=start, end=end, inclusive_end=True)


def merge_overlapping(ranges: Iterable[DateRange]) -> list[DateRange]:
    """Merge overlapping or touching ranges."""

    normalized = [
        (r if r.inclusive_end else DateRange(r.start, r.end - timedelta(days=1)))
        for r in ranges
    ]
    if not normalized:
        return []

    normalized.sort(key=lambda r: (r.start, r.end))
    out: list[DateRange] = [normalized[0]]

    for r in normalized[1:]:
        last = out[-1]
        if r.start <= last.end + timedelta(days=1):
            out[-1] = DateRange(last.start, max(last.end, r.end), inclusive_end=True)
        else:
            out.append(r)

    return out
