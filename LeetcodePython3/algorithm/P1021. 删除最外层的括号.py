#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 16:50
FileName: P1021. 删除最外层的括号.py
Description:
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, index = [], []
        for i, ch in enumerate(s):
            if ch == '(' and len(stack) == 0:
                index.append(i)
            if ch == ')' and len(stack) == 1:
                index.append(i)
            if ch == ')':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(ch for i, ch in enumerate(s) if i not in index)


if __name__ == '__main__':
    solution = Solution().removeOuterParentheses(s="(()())(())")
    print(solution)
