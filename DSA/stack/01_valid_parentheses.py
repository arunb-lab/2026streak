"""DSA - Stack: Valid Parentheses

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

Approach:
Use a stack of opening brackets. When we see a closing bracket, it must match
the most recent opening bracket.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    pairs = {")": "(",
        "]": "[",
        "}": "{",
    }

    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
            continue

        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
            continue

        raise ValueError(f"invalid character: {ch!r}")

    return not stack


if __name__ == "__main__":
    assert is_valid_parentheses("()") is True
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False
    assert is_valid_parentheses("{[]}") is True
    print("ok")
