#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 18:29
FileName: LCR 036. 逆波兰表达式求值
Description:
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a, b, stack = -1, -1, []
        calc = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a / b)
        }
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                stack.append(calc[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    solution = Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(solution)
