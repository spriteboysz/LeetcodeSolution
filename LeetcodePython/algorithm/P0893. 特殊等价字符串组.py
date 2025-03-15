#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 10:37
FileName: algorithm/P0893. 特殊等价字符串组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def process(s):
            ss = [''] * len(s)
            ss[::2] = sorted([ch for i, ch in enumerate(s) if i % 2 == 0])
            ss[1::2] = sorted([ch for i, ch in enumerate(s) if i % 2 == 1])
            return ''.join(ss)

        return len(set(map(process, words)))


if __name__ == '__main__':
    solution = Solution().numSpecialEquivGroups(words=["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"])
    ic(solution)
