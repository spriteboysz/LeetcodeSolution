#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:56
FileName: LC/LCR 018. 验证回文串.py
Description: 
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [c for c in s.lower() if c.isalnum()]
        return ss == ss[::-1]


if __name__ == '__main__':
    solution = Solution().isPalindrome(s="A man, a plan, a canal: Panama")
    print(solution)
