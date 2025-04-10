#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-09 23:43
FileName: LCR/LCR 105. 岛屿的最大面积.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                return 0
            area = 1
            grid[x][y] = -1
            for dx, dy in directions:
                area += dfs(x + dx, y + dy)
            return area

        areas = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue
                areas.append(dfs(i, j))
        return max(areas) if areas else 0


if __name__ == '__main__':
    solution = Solution().maxAreaOfIsland(
        grid=
        [
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
    ic(solution)
