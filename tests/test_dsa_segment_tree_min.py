import pytest

from project.dsa.segment_tree_min import SegmentTreeMin


def test_segment_tree_min_basic() -> None:
    st = SegmentTreeMin([5, 2, 6, 3, 1, 4])
    assert st.range_min(0, 6) == 1.0
    assert st.range_min(0, 2) == 2.0
    assert st.range_min(2, 4) == 3.0

    st.update(4, 10)
    assert st.range_min(0, 6) == 2.0


def test_segment_tree_min_empty_range_returns_inf() -> None:
    st = SegmentTreeMin([1, 2, 3])
    assert st.range_min(1, 1) == float("inf")


def test_segment_tree_min_validation() -> None:
    st = SegmentTreeMin([1, 2, 3])
    with pytest.raises(ValueError):
        st.range_min(-1, 2)
    with pytest.raises(ValueError):
        st.range_min(2, 1)
    with pytest.raises(ValueError):
        st.range_min(0, 4)

    with pytest.raises(IndexError):
        st.update(99, 0)
