#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:08
FileName: P1544. 整理字符串
Description:
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif abs(ord(stack[-1])-ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

if __name__ == '__main__':
    solution = Solution().makeGood(s = "leEeetcode")
    print(solution)