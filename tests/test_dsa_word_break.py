from project.dsa.word_break import word_break


def test_word_break_examples() -> None:
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_word_break_empty_string() -> None:
    assert word_break("", ["a"]) is True


def test_word_break_empty_dict_nonempty_string() -> None:
    assert word_break("a", []) is False
