#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-05 22:16
FileName: algorithm/P3242. 设计相邻元素求和服务.py
Description: 
"""
from functools import lru_cache
from typing import List

from icecream import ic


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    @lru_cache
    def position(self, num):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == num:
                    return i, j
        raise ValueError('Error')

    def adjacentSum(self, value: int) -> int:
        x, y = self.position(value)
        ss = 0
        if x - 1 >= 0:
            ss += self.grid[x - 1][y]
        if x + 1 < len(self.grid):
            ss += self.grid[x + 1][y]
        if y - 1 >= 0:
            ss += self.grid[x][y - 1]
        if y + 1 < len(self.grid[0]):
            ss += self.grid[x][y + 1]
        return ss

    def diagonalSum(self, value: int) -> int:
        x, y = self.position(value)
        ss = 0
        if x - 1 >= 0 and y - 1 >= 0:
            ss += self.grid[x - 1][y - 1]
        if x - 1 >= 0 and y + 1 < len(self.grid[0]):
            ss += self.grid[x - 1][y + 1]
        if x + 1 < len(self.grid) and y - 1 >= 0:
            ss += self.grid[x + 1][y - 1]
        if x + 1 < len(self.grid) and y + 1 < len(self.grid[0]):
            ss += self.grid[x + 1][y + 1]
        return ss


if __name__ == '__main__':
    solution = NeighborSum(grid=[[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    ic(solution.adjacentSum(1))
    ic(solution.adjacentSum(4))
    ic(solution.diagonalSum(4))
    ic(solution.diagonalSum(8))
