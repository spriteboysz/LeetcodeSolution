#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-26 23:38
FileName: P0062. 不同路径
Description:
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().uniquePaths(3, 7)
    print(solution)
