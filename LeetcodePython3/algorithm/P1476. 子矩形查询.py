#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 17:45
FileName: algorithm/P1476. 子矩形查询.py
Description: 
"""
from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            self.matrix[i][col1:col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]


if __name__ == '__main__':
    solution = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    solution.updateSubrectangle(0, 0, 3, 2, 5)
    print(solution.getValue(0, 2))
