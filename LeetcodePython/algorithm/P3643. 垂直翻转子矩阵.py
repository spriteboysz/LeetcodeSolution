#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-18 22:59
FileName: P3643. 垂直翻转子矩阵.py
Description:
"""
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            grid[x + i][y:y + k], grid[x + k - i - 1][y:y + k] = grid[x + k - i - 1][y:y + k], grid[x + i][y:y + k]
        return grid


if __name__ == '__main__':
    s = Solution().reverseSubmatrix(
        grid=[[3, 4, 2, 3], [2, 3, 4, 2]], x=0, y=2, k=2
    )
    print(s)
