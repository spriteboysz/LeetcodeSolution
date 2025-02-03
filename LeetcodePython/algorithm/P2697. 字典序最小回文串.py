#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 20:38
FileName: P2697. 字典序最小回文串
Description:
"""

from icecream import ic


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ss = list(s)
        for i in range(len(ss) // 2):
            a, b = ss[i], ss[len(ss) - 1 - i]
            ss[i] = ss[len(ss) - 1 - i] = min(a, b)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().makeSmallestPalindrome(s="abcd")
    ic(solution)
