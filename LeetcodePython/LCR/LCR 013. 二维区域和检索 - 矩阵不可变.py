#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-14 23:41
FileName: LCR/LCR 013. 二维区域和检索 - 矩阵不可变.py
Description: 
"""
from typing import List

from icecream import ic


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.grid[i + 1][j + 1] = matrix[i][j] + self.grid[i + 1][j] + self.grid[i][j + 1] - self.grid[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2 + 1][col2 + 1] + self.grid[row1][col1] - self.grid[row2 + 1][col1] - \
            self.grid[row1][col2 + 1]


if __name__ == '__main__':
    num_matrix = NumMatrix(
        [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]]
    )
    ic(num_matrix.sumRegion(2, 1, 4, 3))
    ic(num_matrix.sumRegion(1, 1, 2, 2))
    ic(num_matrix.sumRegion(1, 2, 2, 4))
