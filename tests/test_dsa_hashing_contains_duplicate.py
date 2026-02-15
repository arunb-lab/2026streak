from project.dsa.hashing_contains_duplicate import contains_duplicate


def test_contains_duplicate_basic() -> None:
    assert contains_duplicate([1, 2, 3]) is False
    assert contains_duplicate([1, 2, 2, 3]) is True


def test_contains_duplicate_empty_and_singleton() -> None:
    assert contains_duplicate([]) is False
    assert contains_duplicate([42]) is False


def test_contains_duplicate_iterable() -> None:
    assert contains_duplicate(x for x in ["a", "b", "c"]) is False
    assert contains_duplicate(x for x in ["a", "b", "a"]) is True
