#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:35
FileName: P3174. 清除数字.py
Description:
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().clearDigits(s="cb34")
    print(solution)
