from project.dsa.min_window_substring import min_window


def test_min_window_examples() -> None:
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""


def test_min_window_with_duplicates() -> None:
    assert min_window("aaabdabcefaecbef", "abc") == "abc"
    assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
