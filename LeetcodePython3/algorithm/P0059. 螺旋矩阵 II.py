#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 17:02
FileName: algorithm/P0059. 螺旋矩阵 II.py
Description: 
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid = [[0] * n for _ in range(n)]
        x, y, direction = 0, 0, 0
        for i in range(n * n):
            grid[x][y] = i + 1
            dx, dy = directions[direction]
            x1, y1 = x + dx, y + dy
            if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n or grid[x1][y1] > 0:
                direction = (direction + 1) % 4
                dx, dy = directions[direction]
            x, y = x + dx, y + dy

        return grid


if __name__ == '__main__':
    solution = Solution().generateMatrix(4)
    print(solution)
    for row in solution:
        print('\t'.join(map(str, row)))
