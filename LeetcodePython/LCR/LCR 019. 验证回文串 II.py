#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 14:05
FileName: LCR 019. 验证回文串 II
Description:
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(ss):
            return ss == ss[::-1]

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return check(s[:i] + s[i + 1:]) or check(s[:len(s) - 1 - i] + s[len(s) - i:])
        return True


if __name__ == '__main__':
    solution = Solution().validPalindrome(s="abca")
    print(solution)
