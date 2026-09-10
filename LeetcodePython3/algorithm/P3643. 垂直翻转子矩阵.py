#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 09:08
FileName: algorithm/P3643. 垂直翻转子矩阵.py
Description: 
"""
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i0, i1 = x, x + k - 1
        while i0 < i1:
            grid[i0][y:y + k], grid[i1][y:y + k] = grid[i1][y:y + k], grid[i0][y:y + k]
            i0, i1 = i0 + 1, i1 - 1
        return grid


if __name__ == '__main__':
    solution = Solution().reverseSubmatrix(
        grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        x=1, y=0, k=3
    )
    print('<None>' if solution is None else f'{solution=}')
