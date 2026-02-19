from project.dsa.rabin_karp import rabin_karp_find_all


def test_rabin_karp_basic() -> None:
    assert rabin_karp_find_all("aaaaa", "aa") == [0, 1, 2, 3]
    assert rabin_karp_find_all("hello", "ll") == [2]
    assert rabin_karp_find_all("hello", "world") == []


def test_rabin_karp_empty_pattern() -> None:
    assert rabin_karp_find_all("abc", "") == [0, 1, 2, 3]


def test_rabin_karp_pattern_longer_than_text() -> None:
    assert rabin_karp_find_all("ab", "abcd") == []
