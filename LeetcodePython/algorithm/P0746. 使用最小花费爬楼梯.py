#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 10:13
FileName: algorithm/P0746. 使用最小花费爬楼梯.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = 0, 0
        for i in range(2, len(cost) + 1):
            f2 = min(f0 + cost[i - 2], f1 + cost[i - 1])
            f0, f1 = f1, f2
        return f1


if __name__ == '__main__':
    solution = Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    ic(solution)
