#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-18 23:14
FileName: algorithm/P0695. 岛屿的最大面积.py
Description: 
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                return 0
            area = 1
            grid[x][y] = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                area += dfs(x + dx, y + dy)
            return area

        n, m = len(grid), len(grid[0])
        maximum = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maximum = max(maximum, dfs(i, j))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    )
    print(solution)
