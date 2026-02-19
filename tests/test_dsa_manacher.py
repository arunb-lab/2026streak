from project.dsa.manacher import longest_palindromic_substring


def test_longest_palindromic_substring_basic() -> None:
    out = longest_palindromic_substring("babad")
    assert out in {"bab", "aba"}


def test_longest_palindromic_substring_even() -> None:
    assert longest_palindromic_substring("cbbd") == "bb"


def test_longest_palindromic_substring_edge_cases() -> None:
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("aaaa") == "aaaa"
