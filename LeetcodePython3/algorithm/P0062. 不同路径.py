#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 22:55
FileName: P0062. 不同路径.py
Description:
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().uniquePaths(3, 7)
    print(solution)
