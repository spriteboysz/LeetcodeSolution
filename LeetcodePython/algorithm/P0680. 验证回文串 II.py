#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:00
FileName: P0680. 验证回文串 II
Description:
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            return s == s[::-1]

        if check(s):
            return True
        n = len(s)
        for i in range(n // 2):
            j = n - i - 1
            if s[i] != s[j]:
                return check(s[:i] + s[i + 1:]) or check(s[:j] + s[j + 1:])
        return True


if __name__ == '__main__':
    solution = Solution().validPalindrome(s="abca")
    print(solution)
    solution = Solution().validPalindrome(s="aba")
    print(solution)
