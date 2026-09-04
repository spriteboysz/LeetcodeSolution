#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:59
FileName: LC/LCR 019. 验证回文串 II.py
Description: 
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(ss: str) -> bool:
            return ss == ss[::-1]

        n = len(s)
        for i in range(len(s) // 2 + 1):
            if s[i] != s[-1 - i]:
                return check(s[:i] + s[i + 1:]) or check(s[:n - 1 - i] + s[n - i:])
        return True


if __name__ == '__main__':
    solution = Solution().validPalindrome(s="eccer")
    print(solution)
