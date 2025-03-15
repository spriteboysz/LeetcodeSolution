#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 20:11
FileName: algorithm/P0921. 使括号有效的最少添加.py
Description: 
"""

from icecream import ic


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)


if __name__ == '__main__':
    solution = Solution().minAddToMakeValid(s="())")
    ic(solution)
