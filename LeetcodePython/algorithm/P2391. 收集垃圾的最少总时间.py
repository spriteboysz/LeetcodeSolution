#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-24 23:07
FileName: algorithm/P2391. 收集垃圾的最少总时间.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def calc(g):
            cnt = ''.join(garbage).count(g)
            last = [i for i, el in enumerate(garbage) if g in el]
            if last:
                cnt += sum(travel[:last[-1]])
            return cnt

        return sum(calc(el) for el in ['G', 'P', 'M'])


if __name__ == '__main__':
    solution = Solution().garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3])
    ic(solution)
