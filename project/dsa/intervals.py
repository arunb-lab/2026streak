"""Interval algorithms (merge + insert).

Many DSA problems reduce to working with half-open or closed intervals.
This module uses **closed** intervals [start, end] with start <= end.

Includes:
- ``merge_intervals``: merge overlaps.
- ``insert_interval``: insert one interval then merge.

Time complexity: O(n log n) due to sort.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Interval:
    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start > self.end:
            raise ValueError("start must be <= end")


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    """Merge overlapping closed intervals."""
    if not intervals:
        return []

    intervals_sorted = sorted(intervals, key=lambda it: (it.start, it.end))
    out: list[Interval] = [intervals_sorted[0]]

    for it in intervals_sorted[1:]:
        last = out[-1]
        if it.start <= last.end:
            out[-1] = Interval(last.start, max(last.end, it.end))
        else:
            out.append(it)

    return out


def insert_interval(intervals: list[Interval], new: Interval) -> list[Interval]:
    """Insert ``new`` into a list of intervals and merge overlaps."""
    return merge_intervals([*intervals, new])
