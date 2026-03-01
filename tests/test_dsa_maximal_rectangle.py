from project.dsa.maximal_rectangle import maximal_rectangle


def test_maximal_rectangle_examples() -> None:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert maximal_rectangle(matrix) == 6


def test_maximal_rectangle_simple() -> None:
    assert maximal_rectangle([["0"]]) == 0
    assert maximal_rectangle([["1"]]) == 1
    assert maximal_rectangle([["1", "1", "1"]]) == 3
