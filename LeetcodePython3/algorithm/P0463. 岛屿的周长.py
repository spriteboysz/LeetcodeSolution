#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 11:15
FileName: P0463. 岛屿的周长.py
Description:
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 0:
                    continue
                perimeter += 1 if i == 0 else 1 - grid[i - 1][j]
                perimeter += 1 if i == len(grid) - 1 else 1 - grid[i + 1][j]
                perimeter += 1 if j == 0 else 1 - grid[i][j - 1]
                perimeter += 1 if j == len(row) - 1 else 1 - grid[i][j + 1]
        return perimeter


if __name__ == '__main__':
    solution = Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    print(solution)
