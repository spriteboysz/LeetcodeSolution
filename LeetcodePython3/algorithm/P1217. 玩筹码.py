#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:09
FileName: algorithm/P1217. 玩筹码.py
Description: 
"""

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counters = [0, 0]
        for pos in position:
            counters[pos % 2] += 1
        return min(counters)


if __name__ == '__main__':
    solution = Solution().minCostToMoveChips([2, 2, 2, 3, 3])
    print('<None>' if solution is None else f'{solution=}')
