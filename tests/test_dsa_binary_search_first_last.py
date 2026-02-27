from project.dsa.binary_search_first_last import first_last_position


def test_first_last_position_basic() -> None:
    assert first_last_position([5, 7, 7, 8, 8, 10], 8) == (3, 4)
    assert first_last_position([5, 7, 7, 8, 8, 10], 6) == (-1, -1)
    assert first_last_position([], 0) == (-1, -1)


def test_first_last_position_singleton() -> None:
    assert first_last_position([1], 1) == (0, 0)
    assert first_last_position([1], 2) == (-1, -1)


def test_first_last_position_all_same() -> None:
    assert first_last_position([2, 2, 2, 2], 2) == (0, 3)
