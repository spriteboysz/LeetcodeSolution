#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:37
FileName: P0392. 判断子序列.py
Description:
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos1 = pos2 = 0
        while pos1 < len(s) and pos2 < len(t):
            if s[pos1] == t[pos2]:
                pos1 += 1
            pos2 += 1
        return pos1 == len(s)


if __name__ == '__main__':
    solution = Solution().isSubsequence(s="b", t="abc")
    print(solution)
