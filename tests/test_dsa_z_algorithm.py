from project.dsa.z_algorithm import z_find_all, z_function


def test_z_function_known() -> None:
    # Example: s = "aabcaabxaaaz"
    assert z_function("aabcaabxaaaz")[:5] == [0, 1, 0, 0, 3]


def test_z_find_all_basic() -> None:
    assert z_find_all("aaaaa", "aa") == [0, 1, 2, 3]
    assert z_find_all("abcxabcdabcdabcy", "abcdabcy") == [8]
    assert z_find_all("hello", "world") == []


def test_z_find_all_empty_pattern() -> None:
    assert z_find_all("abc", "") == [0, 1, 2, 3]
