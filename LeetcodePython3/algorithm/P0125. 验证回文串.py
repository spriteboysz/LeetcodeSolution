#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:10
FileName: P0125. 验证回文串.py
Description:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch for ch in s.lower() if ch.isalnum()]
        return s == s[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
    print(solution)
