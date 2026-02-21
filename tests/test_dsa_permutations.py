from project.dsa.permutations import permutations


def test_permutations_basic() -> None:
    r = permutations([1, 2, 3])
    assert len(r) == 6
    assert sorted(r) == sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )


def test_permutations_empty() -> None:
    assert permutations([]) == [[]]
