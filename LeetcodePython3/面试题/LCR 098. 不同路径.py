#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:45
FileName: 面试题/LCR 098. 不同路径.py
Description: 
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().uniquePaths(3, 7)
    print('<None>' if not solution else f'{solution=}')
