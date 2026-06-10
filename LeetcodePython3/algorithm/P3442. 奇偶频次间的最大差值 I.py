#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:16
FileName: P3442. 奇偶频次间的最大差值 I.py
Description:
"""
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        return max(el for el in counter.values() if el % 2 == 1) - min(el for el in counter.values() if el % 2 == 0)


if __name__ == '__main__':
    solution = Solution().maxDifference(s="aaaaabbc")
    print(solution)
