#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 15:31
FileName: algorithm/P3560. 木材运输的最小成本.py
Description: 
"""


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if k >= n and k >= m:
            return 0

        return (max(n, m) - k) * k


if __name__ == '__main__':
    solution = Solution()
    print('<None>' if solution is None else f'{solution=}')
