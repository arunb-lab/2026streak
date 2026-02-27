"""Valid parentheses.

Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


_PAIR: dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
}


def is_valid_parentheses(s: str) -> bool:
    stack: list[str] = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
            continue

        opening = _PAIR.get(ch)
        if opening is None:
            # Non-bracket characters are treated as invalid for this classic problem.
            return False

        if not stack or stack.pop() != opening:
            return False

    return not stack
