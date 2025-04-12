#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-10 23:41
FileName: algorithm/P1254. 统计封闭岛屿的数目.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0:
                return
            grid[x][y] = -1
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        for i in range(0, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1):
                    dfs(i, j)

        cnt = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    cnt += 1
                    dfs(i, j)
        return cnt


if __name__ == '__main__':
    solution = Solution().closedIsland(
        grid=[
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]])
    ic(solution)
