#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 16:17
FileName: algorithm/P2658. 网格图中鱼的最大数目.py
Description: 
"""
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                return 0
            k = grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                k += dfs(x + dx, y + dy)
            return k

        maximum = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                area = dfs(i, j)
                maximum = max(maximum, area)
        return maximum


if __name__ == '__main__':
    solution = Solution().findMaxFish(
        grid=[
            [0, 2, 1, 0],
            [4, 0, 0, 3],
            [1, 0, 0, 4],
            [0, 3, 2, 0]
        ]
    )
    print('<None>' if solution is None else f'{solution=}')
