from project.dsa.kmp import kmp_find_all, prefix_function


def test_prefix_function() -> None:
    assert prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    assert prefix_function("") == []


def test_kmp_find_all_basic() -> None:
    assert kmp_find_all("aaaaa", "aa") == [0, 1, 2, 3]
    assert kmp_find_all("abcxabcdabcdabcy", "abcdabcy") == [8]
    assert kmp_find_all("hello", "world") == []


def test_kmp_empty_pattern_matches_everywhere() -> None:
    assert kmp_find_all("abc", "") == [0, 1, 2, 3]
