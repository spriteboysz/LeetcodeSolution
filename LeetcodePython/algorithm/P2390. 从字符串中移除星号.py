#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-12 23:19
FileName: P2390. 从字符串中移除星号
Description:
"""

from icecream import ic


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
    solution = Solution().removeStars(s="leet**cod*e")
    ic(solution)
