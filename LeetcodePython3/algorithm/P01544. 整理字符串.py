#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 12:09
FileName: P01544. 整理字符串.py
Description:
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().makeGood("leEeetcode")
    print(solution)
