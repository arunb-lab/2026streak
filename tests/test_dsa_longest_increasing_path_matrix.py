from project.dsa.longest_increasing_path_matrix import longest_increasing_path


def test_longest_increasing_path_examples() -> None:
    assert (
        longest_increasing_path(
            [
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1],
            ]
        )
        == 4
    )

    assert longest_increasing_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4


def test_longest_increasing_path_empty() -> None:
    assert longest_increasing_path([]) == 0
