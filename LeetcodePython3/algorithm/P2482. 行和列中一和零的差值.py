#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 15:56
FileName: P2482. 行和列中一和零的差值.py
Description:
"""
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = [sum(row) for row in grid]
        columns = [sum(column) for column in zip(*grid)]
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                grid[i][j] = 2 * rows[i] + 2 * columns[j] - (m + n)
        return grid


if __name__ == '__main__':
    solution = Solution().onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]])
    print(solution)
