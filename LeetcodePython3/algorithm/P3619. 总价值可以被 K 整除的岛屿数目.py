#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-18 23:38
FileName: algorithm/P3619. 总价值可以被 K 整除的岛屿数目.py
Description: 
"""
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(x: int, y: int):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                return 0
            val = grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                val += dfs(x + dx, y + dy)
            return val

        n, m = len(grid), len(grid[0])
        values = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    values.append(dfs(i, j))
        return sum(value % k == 0 for value in values)


if __name__ == '__main__':
    solution = Solution().countIslands(
        grid=[
            [0, 2, 1, 0, 0],
            [0, 5, 0, 0, 5],
            [0, 0, 1, 0, 0],
            [0, 1, 4, 7, 0],
            [0, 2, 0, 0, 8]
        ],
        k=5
    )
    print(solution)
