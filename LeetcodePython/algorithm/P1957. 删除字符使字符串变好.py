#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 22:16
FileName: P1957. 删除字符使字符串变好
Description:
"""

from icecream import ic


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) >= 2 and stack[-1] == stack[-2] and stack[-1] == ch:
                pass
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().makeFancyString("aaabaaaa")
    ic(solution)
