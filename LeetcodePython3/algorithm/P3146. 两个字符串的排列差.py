#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:37
FileName: P3146. 两个字符串的排列差.py
Description:
"""
from string import ascii_lowercase


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(s.find(ch) - t.find(ch)) for ch in ascii_lowercase)


if __name__ == '__main__':
    solution = Solution().findPermutationDifference(s="abcde", t="edbac")
    print(solution)
