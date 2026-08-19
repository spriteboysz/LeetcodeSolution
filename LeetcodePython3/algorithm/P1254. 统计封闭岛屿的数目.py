#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-18 23:25
FileName: algorithm/P1254. 统计封闭岛屿的数目.py
Description: 
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 1:
                return
            grid[x][y] = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + dx, y + dy)

        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j] == 0:
                        dfs(i, j)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cnt += 1
                    dfs(i, j)
        return cnt


if __name__ == '__main__':
    solution = Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0]]
    )
    print(solution)
