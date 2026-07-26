#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 09:10
FileName: P0746. 使用最小花费爬楼梯.py
Description:
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(solution)
