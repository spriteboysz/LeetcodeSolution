#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-08 22:00
FileName: P2482. 行和列中一和零的差值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, columns = [0 for _ in range(m)], [0 for _ in range(n)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                rows[i] += num
                columns[j] += num

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = 2 * rows[i] - n + 2 * columns[j] - m
        return matrix


if __name__ == '__main__':
    solution = Solution().onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]])
    ic(solution)
