#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 22:45
FileName: P0150. 逆波兰表达式求值
Description:
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
            else:
                a, b = -1, -1
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    solution = Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(solution)
