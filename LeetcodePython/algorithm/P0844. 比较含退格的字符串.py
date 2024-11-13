#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 20:50
FileName: P0844. 比较含退格的字符串
Description:
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            stack = []
            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)

        return process(s) == process(t)


if __name__ == '__main__':
    solution = Solution().backspaceCompare(s="y#fo##f", t="y#f#o##f")
    print(solution)
