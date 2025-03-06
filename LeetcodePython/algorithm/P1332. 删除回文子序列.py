#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 23:11
FileName: algorithm/P1332. 删除回文子序列.py
Description: 
"""

from icecream import ic


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


if __name__ == '__main__':
    solution = Solution().removePalindromeSub('abba')
    ic(solution)
