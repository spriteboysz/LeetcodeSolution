#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-22 23:01
FileName: algorithm/P1020. 飞地的数量.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 0
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    dfs(i, j)

        return sum(sum(row) for row in grid)


if __name__ == '__main__':
    solution = Solution().numEnclaves(
        grid=[
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ])
    ic(solution)
