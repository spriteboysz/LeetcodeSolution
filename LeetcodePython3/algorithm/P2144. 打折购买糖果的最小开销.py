#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 21:00
FileName: algorithm/P2144. 打折购买糖果的最小开销.py
Description: 
"""
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])


if __name__ == '__main__':
    solution = Solution().minimumCost(cost=[6, 5, 7, 9, 2, 2])
    print(solution)
