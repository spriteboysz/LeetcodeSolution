#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 9:48
FileName: algorithm/P0392. 判断子序列.py
Description: 
"""

from icecream import ic


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        position = 0
        for i, ch in enumerate(t):
            if ch == s[position]:
                position += 1
            if position == len(s):
                return True
        return position == len(s)


if __name__ == '__main__':
    solution = Solution().isSubsequence(s="abc", t="ahbgdc")
    ic(solution)
