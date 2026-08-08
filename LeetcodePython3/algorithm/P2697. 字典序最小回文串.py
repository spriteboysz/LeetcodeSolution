#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-08 12:30
FileName: P2697. 字典序最小回文串.py
Description:
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ss = list(s)
        for i in range(len(ss) // 2):
            ch = min(ss[i], ss[-1 - i])
            ss[i] = ss[-1 - i] = ch
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().makeSmallestPalindrome(s="egcfe")
    print(solution)
