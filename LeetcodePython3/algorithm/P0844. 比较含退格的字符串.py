#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 12:53
FileName: P0844. 比较含退格的字符串.py
Description:
"""


class Solution:
    @staticmethod
    def process(s: str):
        stack = []
        for ch in s:
            if stack and ch == '#':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack).lstrip('#')

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)


if __name__ == '__main__':
    solution = Solution().backspaceCompare(s="y#fo##f", t="y#f#o##f")
    print(solution)
