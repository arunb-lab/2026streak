from project.dsa.set_matrix_zeroes import set_matrix_zeroes


def test_set_matrix_zeroes_example() -> None:
    m = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    set_matrix_zeroes(m)
    assert m == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]


def test_set_matrix_zeroes_first_row_col() -> None:
    m = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    set_matrix_zeroes(m)
    assert m == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
