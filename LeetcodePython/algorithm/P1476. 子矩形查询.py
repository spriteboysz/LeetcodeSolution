#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 15:44
FileName: algorithm/P1476. 子矩形查询.py
Description: 
"""
from typing import List

from icecream import ic


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in self.grid[row1:row2 + 1]:
            row[col1:col2 + 1] = [newValue] * (col2 + 1 - col1)

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]


if __name__ == '__main__':
    solution = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    ic(solution.getValue(0, 2))
    solution.updateSubrectangle(0, 0, 3, 2, 5)
    ic(solution.getValue(0, 2))
    ic(solution.getValue(3, 1))
    solution.updateSubrectangle(3, 0, 3, 2, 10)
    ic(solution.getValue(0, 2))
    ic(solution.getValue(3, 1))
