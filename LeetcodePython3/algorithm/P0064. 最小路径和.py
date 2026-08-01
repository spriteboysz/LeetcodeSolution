#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 15:01
FileName: P0064. 最小路径和.py
Description:
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(solution)
