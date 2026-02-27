from project.dsa.valid_parentheses import is_valid_parentheses


def test_is_valid_parentheses_basic() -> None:
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    assert is_valid_parentheses("{[]}") is True


def test_is_valid_parentheses_edge_cases() -> None:
    assert is_valid_parentheses("") is True
    assert is_valid_parentheses("(") is False
    assert is_valid_parentheses(")") is False


def test_is_valid_parentheses_rejects_non_brackets() -> None:
    assert is_valid_parentheses("(a)") is False
