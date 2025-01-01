#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 19:50
FileName: LCR 098. 不同路径
Description:
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().uniquePaths(3, 7)
    print(solution)
