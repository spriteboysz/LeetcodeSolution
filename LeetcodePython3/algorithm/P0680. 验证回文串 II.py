#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 12:01
FileName: P0680. 验证回文串 II.py
Description:
"""


class Solution:
    @classmethod
    def check(cls, s: str):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return self.check(s[:i] + s[i + 1:]) or self.check(s[:j] + s[j + 1:])
        return True


if __name__ == '__main__':
    solution = Solution().validPalindrome(s="abca")
    print(solution)
