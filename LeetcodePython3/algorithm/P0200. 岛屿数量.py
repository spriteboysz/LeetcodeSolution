#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-18 23:03
FileName: algorithm/P0200. 岛屿数量.py
Description: 
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x: int, y: int):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt


if __name__ == '__main__':
    solution = Solution().numIslands(
        grid=[
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
    )
    print(solution)
