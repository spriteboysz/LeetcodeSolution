#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-05 17:16
FileName: algorithm/P3560. 木材运输的最小成本.py
Description: 
"""

from icecream import ic


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        maximum = max(n, m)
        return 0 if maximum <= k else (maximum - k) * k


if __name__ == '__main__':
    solution = Solution().minCuttingCost(6, 5, 5)
    ic(solution)
