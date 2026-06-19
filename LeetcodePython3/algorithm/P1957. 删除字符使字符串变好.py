#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 11:44
FileName: P1957. 删除字符使字符串变好.py
Description:
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) >= 2 and ch == stack[-1] == stack[-2]:
                continue
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().makeFancyString(s="leeetcode")
    print(solution)
