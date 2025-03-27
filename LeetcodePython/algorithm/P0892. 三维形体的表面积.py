#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-27 22:49
FileName: algorithm/P0892. 三维形体的表面积.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def calc(high, x, y):
            area = 0 if high == 0 else 2
            area += high if x - 1 < 0 else max(0, high - grid[x - 1][y])
            area += high if x + 1 >= len(grid) else max(0, high - grid[x + 1][y])
            area += high if y - 1 < 0 else max(0, high - grid[x][y - 1])
            area += high if y + 1 >= len(grid[0]) else max(0, high - grid[x][y + 1])
            return area

        return sum(calc(num, i, j) for i, row in enumerate(grid) for j, num in enumerate(row))


if __name__ == '__main__':
    solution = Solution().surfaceArea([[1, 2], [3, 4]])
    ic(solution)
