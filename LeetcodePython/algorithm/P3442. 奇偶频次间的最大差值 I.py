#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 9:14
FileName: algorithm/P3442. 奇偶频次间的最大差值 I.py
Description: 
"""

from icecream import ic
from collections import defaultdict


class Solution:
    def maxDifference(self, s: str) -> int:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        counter = list(dic.values())
        return max(cnt for cnt in counter if cnt % 2 == 1) - min(cnt for cnt in counter if cnt % 2 == 0)


if __name__ == '__main__':
    solution = Solution().maxDifference('aaaaabbc')
    ic(solution)
