#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:18
FileName: LC/LCR 099. 最小路径和.py
Description: 
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(solution)
