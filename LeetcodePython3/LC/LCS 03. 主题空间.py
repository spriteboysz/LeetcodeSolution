#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 13:43
FileName: 面试题/LCS 03. 主题空间.py
Description: 
"""
from typing import List


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        grid = [list(row) for row in grid]
        n, m = len(grid), len(grid[0])

        def dfs(x, y, v):
            nonlocal flag
            if not (0 <= x < n and 0 <= y < m) or grid[i][j] == '0':
                flag = False
                return 0
            if grid[x][y] != v:
                return 0
            grid[x][y] = '6'
            ans = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ans += dfs(x + dx, y + dy, v)
            return ans

        areas = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0' and grid[i][j] != '6':
                    flag = True
                    area = dfs(i, j, grid[i][j])
                    if flag:
                        areas.append(area)
        return max(areas, default=0)


if __name__ == '__main__':
    solution = Solution().largestArea(["11111100000", "21243101111", "21224101221", "11111101111"])
    print('<None>' if not solution else f'{solution=}')
