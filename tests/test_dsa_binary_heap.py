import pytest

from project.dsa.binary_heap import MinHeap


def test_min_heap_push_pop_sorted() -> None:
    h = MinHeap()
    for x in [5, 3, 8, 1, 2, 7]:
        h.push(x)

    out = [h.pop() for _ in range(6)]
    assert out == sorted(out)
    assert out == [1, 2, 3, 5, 7, 8]


def test_min_heap_peek() -> None:
    h = MinHeap()
    h.push(10)
    h.push(4)
    assert h.peek() == 4
    assert h.pop() == 4
    assert h.peek() == 10


def test_min_heap_empty_errors() -> None:
    h = MinHeap()
    with pytest.raises(IndexError):
        h.peek()
    with pytest.raises(IndexError):
        h.pop()
