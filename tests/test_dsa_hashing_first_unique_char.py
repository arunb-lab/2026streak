from project.dsa.hashing_first_unique_char import first_unique_char_index


def test_first_unique_char_index_basic() -> None:
    assert first_unique_char_index("leetcode") == 0
    assert first_unique_char_index("loveleetcode") == 2


def test_first_unique_char_index_none() -> None:
    assert first_unique_char_index("aabb") == -1


def test_first_unique_char_index_empty() -> None:
    assert first_unique_char_index("") == -1
