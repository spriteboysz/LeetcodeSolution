#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 20:35
FileName: algorithm/P0200. 岛屿数量.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt


if __name__ == '__main__':
    solution = Solution().numIslands(
        grid=[["1", "1", "0", "0", "0"],
              ["1", "1", "0", "0", "0"],
              ["0", "0", "1", "0", "0"],
              ["0", "0", "0", "1", "1"]])
    ic(solution)
