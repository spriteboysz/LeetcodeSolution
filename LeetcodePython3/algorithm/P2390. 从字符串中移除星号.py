#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 10:51
FileName: P2390. 从字符串中移除星号.py
Description:
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().removeStars(s = "leet**cod*e")
    print(solution)
