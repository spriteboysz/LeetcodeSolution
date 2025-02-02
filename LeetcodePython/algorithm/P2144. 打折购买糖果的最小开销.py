#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 21:59
FileName: P2144. 打折购买糖果的最小开销
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])


if __name__ == '__main__':
    solution = Solution().minimumCost(cost=[6, 5, 7, 9, 2, 2])
    ic(solution)
