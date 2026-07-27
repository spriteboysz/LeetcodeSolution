#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 21:01
FileName: P0459. 重复的子字符串.py
Description:
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            div, mod = divmod(n, i)
            if mod == 0 and s[:i] * div == s:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().repeatedSubstringPattern('za')
    print(solution)
