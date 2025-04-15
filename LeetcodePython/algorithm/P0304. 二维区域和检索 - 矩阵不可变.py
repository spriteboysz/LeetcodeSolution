#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-15 22:42
FileName: algorithm/P0304. 二维区域和检索 - 矩阵不可变.py
Description: 
"""
from typing import List

from icecream import ic


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] += matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] += matrix[i - 1][j]
                else:
                    matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
            self.acc = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.acc[row2][col2]
        if row1 == 0:
            return self.acc[row2][col2] - self.acc[row2][col1 - 1]
        if col1 == 0:
            return self.acc[row2][col2] - self.acc[row1 - 1][col2]
        return self.acc[row2][col2] + self.acc[row1 - 1][col1 - 1] - self.acc[row2][col1 - 1] - self.acc[row1 - 1][col2]


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
