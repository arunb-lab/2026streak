"""DSA - Stack: Valid Parentheses

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Rules:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Approach (stack):
- Push opening brackets
- On closing bracket, the stack top must match

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    pair = {")": "(",
        "]": "[",
        "}": "{",
    }
    stack: list[str] = []

    for ch in s:
        if ch in ("(", "[", "{"):
            stack.append(ch)
        else:
            if ch not in pair:
                return False
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    assert is_valid_parentheses("{[]}") is True
    print("ok")
