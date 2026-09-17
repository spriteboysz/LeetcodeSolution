#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 12:16
FileName: algorithm/P1260. 二维网格迁移.py
Description: 
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        k %= n * m
        nums = sum(grid, [])
        nums = nums[-k:] + nums[:-k]
        return [nums[i:i + m] for i in range(0, n * m, m)]


if __name__ == '__main__':
    solution = Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1)
    print('<None>' if solution is None else f'{solution=}')
