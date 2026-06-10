#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 21:32
FileName: P3110. 字符串的分数.py
Description:
"""

from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(ch1) - ord(ch2)) for ch1, ch2 in pairwise(s))


if __name__ == '__main__':
    solution = Solution().scoreOfString('hello')
    print(solution)
