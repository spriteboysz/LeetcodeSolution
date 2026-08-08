#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-08 12:01
FileName: P1863. 找出所有子集的异或总和再求和.py
Description:
"""
from typing import List


class NeighborSum:
    dx = [-1, 1, 1, -1, 0, 1, 0, -1]
    dy = [0, 1, 0, -1, -1, -1, 1, 1]

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.mp = dict()
        for i in range(self.n):
            for j in range(self.n):
                self.mp[grid[i][j]] = (i, j)

    # 上下左右
    def adjacentSum(self, value: int) -> int:
        pos = self.mp.get(value)
        sum_val = 0
        for i in range(0, 8, 2):  # 偏移量
            x, y = pos[0] + self.dx[i], pos[1] + self.dy[i]
            if 0 <= x < self.n and 0 <= y < self.n:
                sum_val += self.grid[x][y]
        return sum_val

    # 两条对角线
    def diagonalSum(self, value: int) -> int:
        pos = self.mp.get(value)
        sum_val = 0
        for i in range(1, 8, 2):  # 偏移量
            x, y = pos[0] + self.dx[i], pos[1] + self.dy[i]
            if 0 <= x < self.n and 0 <= y < self.n:
                sum_val += self.grid[x][y]
        return sum_val
