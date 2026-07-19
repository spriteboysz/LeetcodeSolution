#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 20:20
FileName: P0150. 逆波兰表达式求值.py
Description:
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
            a, b = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            if token == '-':
                stack.append(b - a)
            if token == '*':
                stack.append(a * b)
            if token == '/':
                stack.append(int(b / a))
        return stack.pop()


if __name__ == '__main__':
    solution = Solution().evalRPN(["4", "13", "5", "/", "+"])
    print(solution)
