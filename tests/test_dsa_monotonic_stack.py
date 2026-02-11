from project.dsa.monotonic_stack import (
    largest_rectangle_histogram,
    next_greater_elements,
)


def test_next_greater_elements() -> None:
    assert next_greater_elements([2, 1, 2, 4, 3]) == [4, 2, 4, None, None]
    assert next_greater_elements([]) == []
    assert next_greater_elements([1]) == [None]


def test_largest_rectangle_histogram() -> None:
    assert largest_rectangle_histogram([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_histogram([2, 4]) == 4
    assert largest_rectangle_histogram([1, 1, 1]) == 3
    assert largest_rectangle_histogram([]) == 0
