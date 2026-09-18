#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 16:46
FileName: algorithm/P1020. 飞地的数量.py
Description: 
"""
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                return
            grid[x][y] = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x + dx, y + dy)

        n, m = len(grid), len(grid[0])
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        return sum(sum(grid, []))


if __name__ == '__main__':
    solution = Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    print('<None>' if solution is None else f'{solution=}')
