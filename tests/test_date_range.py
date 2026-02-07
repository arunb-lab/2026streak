from __future__ import annotations

from datetime import date

import pytest

from project.date_range import DateRange, merge_overlapping


def test_inclusive_days_and_contains() -> None:
    r = DateRange(date(2026, 1, 1), date(2026, 1, 3))
    assert r.days() == 3
    assert r.contains(date(2026, 1, 1))
    assert r.contains(date(2026, 1, 3))
    assert not r.contains(date(2025, 12, 31))
    assert not r.contains(date(2026, 1, 4))


def test_exclusive_end_days() -> None:
    r = DateRange(date(2026, 1, 1), date(2026, 1, 4), inclusive_end=False)
    assert r.days() == 3
    assert r.contains(date(2026, 1, 3))
    assert not r.contains(date(2026, 1, 4))


def test_invalid_ranges_raise() -> None:
    with pytest.raises(ValueError):
        DateRange(date(2026, 1, 2), date(2026, 1, 1))

    with pytest.raises(ValueError):
        DateRange(date(2026, 1, 1), date(2026, 1, 1), inclusive_end=False)


def test_business_days() -> None:
    # 2026-01-01 is Thu. Range 1..4 includes Thu,Fri,Sat,Sun => 2 business days.
    r = DateRange(date(2026, 1, 1), date(2026, 1, 4))
    assert r.business_days() == 2


def test_business_days_excluding_holidays() -> None:
    r = DateRange(date(2026, 1, 1), date(2026, 1, 4))
    # Exclude Friday => only Thursday counts.
    assert r.business_days(holidays=[date(2026, 1, 2)]) == 1


def test_shift() -> None:
    r = DateRange(date(2026, 1, 1), date(2026, 1, 3))
    shifted = r.shift(days=2)
    assert shifted.start == date(2026, 1, 3)
    assert shifted.end == date(2026, 1, 5)


def test_split_into_chunks() -> None:
    r = DateRange(date(2026, 1, 1), date(2026, 1, 5))
    chunks = r.split(chunk_days=2)
    assert [c.to_iso() for c in chunks] == [
        "2026-01-01..2026-01-02",
        "2026-01-03..2026-01-04",
        "2026-01-05..2026-01-05",
    ]

    with pytest.raises(ValueError):
        r.split(chunk_days=0)


def test_overlap_and_intersection() -> None:
    a = DateRange(date(2026, 1, 1), date(2026, 1, 10))
    b = DateRange(date(2026, 1, 5), date(2026, 1, 20))
    c = DateRange(date(2026, 2, 1), date(2026, 2, 2))

    assert a.overlaps(b)
    assert not a.overlaps(c)

    inter = a.intersection(b)
    assert inter is not None
    assert inter.start == date(2026, 1, 5)
    assert inter.end == date(2026, 1, 10)


def test_from_iso_to_iso_roundtrip() -> None:
    r = DateRange.from_iso("2026-01-01..2026-01-31")
    assert r.to_iso() == "2026-01-01..2026-01-31"


def test_merge_overlapping_and_touching() -> None:
    ranges = [
        DateRange(date(2026, 1, 1), date(2026, 1, 3)),
        DateRange(date(2026, 1, 4), date(2026, 1, 5)),  # touches (3 then 4)
        DateRange(date(2026, 1, 10), date(2026, 1, 12)),
        DateRange(date(2026, 1, 11), date(2026, 1, 15)),  # overlaps
    ]
    merged = merge_overlapping(ranges)
    assert merged == [
        DateRange(date(2026, 1, 1), date(2026, 1, 5)),
        DateRange(date(2026, 1, 10), date(2026, 1, 15)),
    ]
