#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 10:58
FileName: P1332. 删除回文子序列.py
Description:
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


if __name__ == '__main__':
    solution = Solution().removePalindromeSub(s="ababa")
    print(solution)
