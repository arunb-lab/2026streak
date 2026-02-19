import pytest

from project.dsa.median_of_stream import MedianFinder


def test_median_of_stream_sequence() -> None:
    mf = MedianFinder()

    mf.add(1)
    assert mf.median() == 1.0

    mf.add(2)
    assert mf.median() == 1.5

    mf.add(3)
    assert mf.median() == 2.0

    mf.add(4)
    assert mf.median() == 2.5


def test_median_of_stream_duplicates_and_negatives() -> None:
    mf = MedianFinder()
    for x in [5, -1, -1, 5]:
        mf.add(x)

    assert len(mf) == 4
    assert mf.median() == 2.0  # sorted: [-1,-1,5,5]


def test_median_empty_raises() -> None:
    mf = MedianFinder()
    with pytest.raises(ValueError):
        mf.median()
