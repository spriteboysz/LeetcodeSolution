#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-24 09:19
FileName: algorithm/P3541. 找到频率最高的元音和辅音.py
Description: 
"""
from collections import defaultdict

from icecream import ic


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for ch in s:
            if ch in vowels:
                dic1[ch] += 1
            else:
                dic2[ch] += 1
        return max([0, *dic1.values()]) + max([0, *dic2.values()])


if __name__ == '__main__':
    solution = Solution().maxFreqSum(s="successes")
    ic(solution)
