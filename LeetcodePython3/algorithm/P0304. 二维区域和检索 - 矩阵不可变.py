#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:41
FileName: P0304. 二维区域和检索 - 矩阵不可变.py
Description:
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                grid[i + 1][j + 1] = grid[i][j + 1] + grid[i + 1][j] - grid[i][j] + num
        self.grid = grid

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2 + 1][col2 + 1] - self.grid[row2 + 1][col1] - self.grid[row1][col2 + 1] + self.grid[row1][
            col1]


if __name__ == '__main__':
    solution = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(solution.sumRegion(1, 1, 2, 2))
