import pytest

from project.dsa.sparse_table import SparseTableMin


def test_sparse_table_min_basic_queries() -> None:
    st = SparseTableMin([5, 2, 6, 3, 1, 4])
    assert st.query(0, 1) == 5
    assert st.query(0, 2) == 2
    assert st.query(1, 4) == 2
    assert st.query(2, 5) == 1
    assert st.query(4, 6) == 1


def test_sparse_table_range_validation() -> None:
    st = SparseTableMin([1, 2, 3])

    with pytest.raises(ValueError):
        st.query(-1, 2)
    with pytest.raises(ValueError):
        st.query(2, 1)
    with pytest.raises(ValueError):
        st.query(0, 4)
    with pytest.raises(ValueError):
        st.query(1, 1)


def test_sparse_table_empty_array() -> None:
    st = SparseTableMin([])
    assert st.n == 0
    with pytest.raises(ValueError):
        st.query(0, 0)
