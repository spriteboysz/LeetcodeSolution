#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 22:37
FileName: P0892. 三维形体的表面积.py
Description:
"""
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    continue
                area += 2
                if i == 0:
                    area += v
                else:
                    area += max(0, v - grid[i - 1][j])
                if i == len(grid) - 1:
                    area += v
                else:
                    area += max(0, v - grid[i + 1][j])
                if j == 0:
                    area += v
                else:
                    area += max(0, v - grid[i][j - 1])
                if j == len(row) - 1:
                    area += v
                else:
                    area += max(0, v - grid[i][j + 1])
        return area


if __name__ == '__main__':
    solution = Solution().surfaceArea(grid=[[1, 2], [3, 4]])
    print(solution)
