import pytest

from project.dsa.intervals import Interval, insert_interval, merge_intervals


def test_merge_intervals_basic() -> None:
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    assert merge_intervals(intervals) == [
        Interval(1, 6),
        Interval(8, 10),
        Interval(15, 18),
    ]


def test_merge_intervals_touching_merges_for_closed_intervals() -> None:
    assert merge_intervals([Interval(1, 2), Interval(2, 3)]) == [Interval(1, 3)]


def test_insert_interval() -> None:
    intervals = [Interval(1, 2), Interval(5, 7)]
    assert insert_interval(intervals, Interval(2, 6)) == [Interval(1, 7)]


def test_interval_validation() -> None:
    with pytest.raises(ValueError):
        Interval(3, 2)
