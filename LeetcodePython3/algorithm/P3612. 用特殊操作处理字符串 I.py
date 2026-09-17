#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 17:04
FileName: algorithm/P3612. 用特殊操作处理字符串 I.py
Description: 
"""


class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            elif c == '#':
                stack.extend(stack)
            elif c == '%':
                stack.reverse()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().processStr(s="a#b%*")
    print('<None>' if solution is None else f'{solution=}')
