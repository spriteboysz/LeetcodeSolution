#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 22:51
FileName: P3502. 到达每个位置的最小费用.py
Description:
"""
from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minimum = cost[0]
        for i, c in enumerate(cost):
            minimum = min(minimum, c)
            cost[i] = minimum
        return cost


if __name__ == '__main__':
    solution = Solution().minCosts(cost=[5, 3, 4, 1, 3, 2])
    print(solution)
