"""DSA - Stack: Evaluate Reverse Polish Notation

Problem:
Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
Tokens are either integers or one of: +, -, *, /.
Division truncates toward zero.

Approach:
- Use a stack of ints
- For an operator, pop two operands (a, b), push (a op b)

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for tok in tokens:
        if tok in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                # Python // floors; we want truncation toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression")
    return stack[0]


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("ok")
