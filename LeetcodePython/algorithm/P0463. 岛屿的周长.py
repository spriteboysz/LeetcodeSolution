#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-22 21:42
FileName: algorithm/P0463. 岛屿的周长.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def calc(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 1
            return int(grid[x][y] == 0)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                cnt += calc(i - 1, j) + calc(i + 1, j) + calc(i, j - 1) + calc(i, j + 1)
        return cnt


if __name__ == '__main__':
    solution = Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    ic(solution)
