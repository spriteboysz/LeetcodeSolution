#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:34
FileName: P2373. 矩阵中的局部最大值.py
Description:
"""
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        matrix = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                maximum = max(grid[i + di][j + dj] for di in range(-1, 2) for dj in range(-1, 2))
                matrix[i - 1][j - 1] = maximum
        return matrix


if __name__ == '__main__':
    solution = Solution().largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
    print(solution)
