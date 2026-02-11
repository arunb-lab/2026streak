import pytest

from project.dsa.segment_tree import SegmentTreeSum


def test_segment_tree_query_update() -> None:
    st = SegmentTreeSum([1, 3, 5, 7, 9, 11])
    assert st.query(0, 3) == 9
    assert st.query(3, 6) == 27

    st.update(1, 10)
    assert st.query(0, 3) == 16


def test_segment_tree_range_validation() -> None:
    st = SegmentTreeSum([1, 2, 3])

    with pytest.raises(ValueError):
        st.query(-1, 2)
    with pytest.raises(ValueError):
        st.query(2, 1)
    with pytest.raises(ValueError):
        st.query(0, 4)

    with pytest.raises(IndexError):
        st.update(5, 0)
