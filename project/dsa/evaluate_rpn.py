"""Evaluate Reverse Polish Notation (RPN).

Problem:
You are given an array of strings tokens that represents an arithmetic
expression in Reverse Polish Notation.
Return the integer result.

Supported operators: +, -, *, /
Division truncates toward zero.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate an RPN expression.

    Raises:
        ValueError: if tokens is malformed.
        ZeroDivisionError: if division by zero occurs.
    """

    stack: list[int] = []

    for tok in tokens:
        if tok in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                raise ValueError("malformed RPN: insufficient operands")
            b = stack.pop()
            a = stack.pop()

            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                # Truncate toward zero (Python // truncates toward -inf).
                stack.append(int(a / b))
        else:
            try:
                stack.append(int(tok))
            except ValueError as e:  # pragma: no cover
                raise ValueError(f"invalid token: {tok!r}") from e

    if len(stack) != 1:
        raise ValueError("malformed RPN: leftover operands")

    return stack[0]
