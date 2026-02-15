from project.dsa.hashing_longest_consecutive import longest_consecutive


def test_longest_consecutive_basic() -> None:
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_longest_consecutive_empty() -> None:
    assert longest_consecutive([]) == 0


def test_longest_consecutive_singleton() -> None:
    assert longest_consecutive([42]) == 1
