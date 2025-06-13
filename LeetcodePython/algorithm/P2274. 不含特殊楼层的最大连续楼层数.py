#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-12 23:35
FileName: algorithm/P2274. 不含特殊楼层的最大连续楼层数.py
Description: 
"""
from itertools import pairwise
from typing import List

from icecream import ic


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maximum = max(special[0] - bottom, top - special[-1])
        for x, y in pairwise(special):
            maximum = max(maximum, y - x - 1)
        for x, y in pairwise([1, 2, 3, 4, 5]):
            print(x, y)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxConsecutive(bottom=2, top=9, special=[4, 6])
    ic(solution)
