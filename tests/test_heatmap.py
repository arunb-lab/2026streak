from __future__ import annotations

from datetime import date

import pytest

from project.heatmap import build_heatmap, max_count, weekday_labels


def test_build_heatmap_single_day() -> None:
    h = build_heatmap(date(2026, 1, 1), date(2026, 1, 1), {date(2026, 1, 1): 3})
    assert h.start == date(2026, 1, 1)
    assert h.end == date(2026, 1, 1)
    assert h.height == 7
    assert h.width >= 1
    assert max_count(h) == 3


def test_build_heatmap_fills_missing_as_zero() -> None:
    h = build_heatmap(date(2026, 1, 1), date(2026, 1, 3), {})
    # all cells in-range should exist with count 0
    counts = [c.count for col in h.weeks for c in col if c is not None]
    assert len(counts) == 3
    assert set(counts) == {0}


def test_invalid_range_raises() -> None:
    with pytest.raises(ValueError):
        build_heatmap(date(2026, 1, 2), date(2026, 1, 1), {})


def test_weekday_labels_order() -> None:
    assert weekday_labels(sunday_first=True)[0] == "Sun"
    assert weekday_labels(sunday_first=False)[0] == "Mon"
