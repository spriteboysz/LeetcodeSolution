#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 9:18
FileName: LCR/P3502. 到达每个位置的最小费用.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minimum = [cost[0]]
        for i in range(1, len(cost)):
            minimum.append(min(minimum[-1], cost[i]))
        return minimum


if __name__ == '__main__':
    solution = Solution().minCosts(cost=[5, 3, 4, 1, 3, 2])
    ic(solution)
