from project.dsa.lcs import lcs_length


def test_lcs_length() -> None:
    assert lcs_length("abcde", "ace") == 3
    assert lcs_length("abc", "abc") == 3
    assert lcs_length("abc", "def") == 0
    assert lcs_length("", "abc") == 0
