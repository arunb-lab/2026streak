import pytest

from project.dsa.lazy_segment_tree import LazySegTreeRangeAddSum


def test_lazy_segment_tree_range_add_and_sum() -> None:
    st = LazySegTreeRangeAddSum([1, 2, 3, 4, 5])

    assert st.range_sum(0, 5) == 15
    assert st.range_sum(1, 4) == 9

    st.range_add(1, 4, 10)  # [1,12,13,14,5]
    assert st.range_sum(0, 5) == 45
    assert st.range_sum(1, 4) == 39
    assert st.range_sum(4, 5) == 5

    st.range_add(0, 5, -1)  # [0,11,12,13,4]
    assert st.range_sum(0, 5) == 40
    assert st.range_sum(0, 1) == 0


def test_lazy_segment_tree_validates_ranges() -> None:
    st = LazySegTreeRangeAddSum([1, 2, 3])

    with pytest.raises(ValueError):
        st.range_sum(-1, 2)
    with pytest.raises(ValueError):
        st.range_sum(2, 1)
    with pytest.raises(ValueError):
        st.range_sum(0, 4)

    with pytest.raises(ValueError):
        st.range_add(-1, 2, 1)
    with pytest.raises(ValueError):
        st.range_add(2, 1, 1)
    with pytest.raises(ValueError):
        st.range_add(0, 4, 1)


def test_lazy_segment_tree_empty_queries() -> None:
    st = LazySegTreeRangeAddSum([1, 2, 3])
    assert st.range_sum(1, 1) == 0
    st.range_add(1, 1, 5)  # no-op
    assert st.range_sum(0, 3) == 6
