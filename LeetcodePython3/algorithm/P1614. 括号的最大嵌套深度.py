#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:21
FileName: P1614. 括号的最大嵌套深度.py
Description:
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        stack, maximum = [], 0
        for ch in s:
            if ch not in ['(', ')']:
                continue
            if stack and stack[-1] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append(ch)
            maximum = max(maximum, len(stack))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxDepth(s="(1+(2*3)+((8)/4))+1")
    print(solution)
