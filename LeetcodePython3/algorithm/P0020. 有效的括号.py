#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 13:31
FileName: P0020. 有效的括号.py
Description:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if stack and brackets.get(ch, None) == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == '__main__':
    solution = Solution().isValid(s="()[]{}")
    print(solution)
