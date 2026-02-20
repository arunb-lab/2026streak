import pytest

from project.dsa.min_stack import MinStack


def test_min_stack_push_pop_and_min() -> None:
    s: MinStack[int] = MinStack()

    s.push(3)
    assert s.get_min() == 3

    s.push(5)
    assert s.get_min() == 3

    s.push(2)
    assert s.get_min() == 2

    s.push(2)
    assert s.get_min() == 2

    assert s.pop() == 2
    assert s.get_min() == 2

    assert s.pop() == 2
    assert s.get_min() == 3


def test_min_stack_errors_when_empty() -> None:
    s: MinStack[int] = MinStack()

    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.top()
    with pytest.raises(IndexError):
        s.get_min()

    assert s.try_get_min() is None
