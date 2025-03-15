#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-13 23:28
FileName: algorithm/P1605. 给定行和列的和求可行矩阵.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        return grid


if __name__ == '__main__':
    solution = Solution().restoreMatrix([3, 8], [4, 7])
    ic(solution)
