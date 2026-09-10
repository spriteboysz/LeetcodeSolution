#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 09:58
FileName: 面试题/LCR 105. 岛屿的最大面积.py
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
        return max(dfs(i, j) for i in range(n) for j in range(m))


if __name__ == '__main__':
    solution = Solution().maxAreaOfIsland([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    )
    print('<None>' if not solution else f'{solution=}')
