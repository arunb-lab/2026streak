from project.dsa.hashing_valid_anagram import is_anagram


def test_is_anagram_basic() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False


def test_is_anagram_edge_cases() -> None:
    assert is_anagram("", "") is True
    assert is_anagram("a", "") is False
    assert is_anagram("a", "A") is False
