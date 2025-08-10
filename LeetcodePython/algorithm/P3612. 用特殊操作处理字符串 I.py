#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-10 11:06
FileName: algorithm/P3612. 用特殊操作处理字符串 I.py
Description: 
"""

from icecream import ic


class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            elif ch == '#':
                stack.extend(stack)
            elif ch == '%':
                stack.reverse()
            else:
                stack.append(ch)
        return ''.join(stack)



if __name__ == '__main__':
    solution = Solution().processStr(s="a#b%*")
    ic(solution)
