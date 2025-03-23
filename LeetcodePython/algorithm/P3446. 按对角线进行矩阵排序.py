#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 10:37
FileName: algorithm/P3446. 按对角线进行矩阵排序.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diagonals = [[] for _ in range(m + n)]
        for i in range(m):
            for j in range(n):
                diagonals[m - i + j].append(grid[i][j])
        for i, diagonal in enumerate(diagonals):
            if i <= len(diagonals) // 2:
                diagonal.sort()
            else:
                diagonal.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                grid[i][j] = diagonals[m - i + j].pop()
        return grid


if __name__ == '__main__':
    solution = Solution().sortMatrix(grid=[[1, 7, 3], [9, 8, 2], [4, 5, 6]])
    ic(solution)
