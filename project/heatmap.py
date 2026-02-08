"""GitHub-style contribution heatmap utilities.

This module is intentionally dependency-free.

It provides two layers:
- Pure *data* structures (cells laid out in week-columns x weekday-rows)
- Small helpers to build a year/period heatmap from a mapping of date->count

The goal: a tiny, reusable library you can demo in a portfolio repo.

Week layout:
- Columns are weeks, left-to-right.
- Rows are weekdays, top-to-bottom.
- By default we use **Sunday-first** to match GitHub's public grid.

Python: 3.10+
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Iterable, Mapping


@dataclass(frozen=True, slots=True)
class HeatmapCell:
    day: date
    count: int


@dataclass(frozen=True, slots=True)
class Heatmap:
    """A 2D heatmap grid.

    Attributes:
        weeks: A list of columns; each column is a list of cells for weekdays.
            Missing dates (outside the requested range) are represented as None.
    """

    weeks: list[list[HeatmapCell | None]]
    start: date
    end: date
    sunday_first: bool = True

    @property
    def width(self) -> int:
        return len(self.weeks)

    @property
    def height(self) -> int:
        return 7


def _weekday_index(d: date, *, sunday_first: bool) -> int:
    # Python: Monday=0..Sunday=6
    if sunday_first:
        return (d.weekday() + 1) % 7  # Sunday=0
    return d.weekday()  # Monday=0


def _start_of_week(d: date, *, sunday_first: bool) -> date:
    idx = _weekday_index(d, sunday_first=sunday_first)
    return d - timedelta(days=idx)


def build_heatmap(
    start: date,
    end: date,
    counts: Mapping[date, int] | None = None,
    *,
    sunday_first: bool = True,
) -> Heatmap:
    """Build a week x weekday heatmap for an inclusive date interval."""

    if start > end:
        raise ValueError("start must be <= end")

    counts = counts or {}

    grid_start = _start_of_week(start, sunday_first=sunday_first)

    weeks: list[list[HeatmapCell | None]] = []
    cur = grid_start

    def in_range(x: date) -> bool:
        return start <= x <= end

    while cur <= end:
        col: list[HeatmapCell | None] = [None] * 7
        for i in range(7):
            day = cur + timedelta(days=i)
            if in_range(day):
                col[i] = HeatmapCell(day=day, count=int(counts.get(day, 0)))
        weeks.append(col)
        cur += timedelta(days=7)

    return Heatmap(weeks=weeks, start=start, end=end, sunday_first=sunday_first)


def max_count(h: Heatmap) -> int:
    """Max count across all cells."""

    m = 0
    for col in h.weeks:
        for cell in col:
            if cell is None:
                continue
            if cell.count > m:
                m = cell.count
    return m


def iter_cells(h: Heatmap) -> Iterable[HeatmapCell]:
    for col in h.weeks:
        for cell in col:
            if cell is not None:
                yield cell
