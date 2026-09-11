#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 14:32
FileName: algorithm/P2391. 收集垃圾的最少总时间.py
Description: 
"""
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p1, p2, p3 = 0, 0, 0
        for i, g in enumerate(garbage[1:], start=1):
            if 'G' in g:
                p1 = i
            if 'P' in g:
                p2 = i
            if 'M' in g:
                p3 = i
        return sum(travel[:p1]) + sum(travel[:p2]) + sum(travel[:p3]) + sum(map(len, garbage))


if __name__ == '__main__':
    solution = Solution().garbageCollection(
        garbage=['G', 'P', 'GP', 'GG'], travel=[2, 4, 3]
    )
    print('<None>' if solution is None else f'{solution=}')
