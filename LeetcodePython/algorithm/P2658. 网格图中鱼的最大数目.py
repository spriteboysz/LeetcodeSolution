#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-25 23:06
FileName: algorithm/P2658. 网格图中鱼的最大数目.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maximum = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            cur = grid[x][y]
            grid[x][y] = 0
            for dx, dy in directions:
                cur += dfs(x + dx, y + dy)
            return cur

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                maximum = max(maximum, dfs(i, j))
        return maximum


if __name__ == '__main__':
    solution = Solution().findMaxFish(
        grid=[[0, 2, 1, 0],
              [4, 0, 0, 3],
              [1, 0, 0, 4],
              [0, 3, 2, 0]])
    ic(solution)
