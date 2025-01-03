#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-03 21:30
FileName: LCR 099. 最小路径和
Description:
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(solution)
