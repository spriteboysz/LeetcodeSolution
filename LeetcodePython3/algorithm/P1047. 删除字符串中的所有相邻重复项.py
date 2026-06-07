#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 11:49
FileName: P1047. 删除字符串中的所有相邻重复项.py
Description:
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().removeDuplicates("abbaca")
    print(solution)
