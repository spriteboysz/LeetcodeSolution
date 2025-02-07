#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:14
FileName: P2373. 矩阵中的局部最大值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        largest = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i in range(0, n - 2):
            for j in range(0, n - 2):
                for dx in range(3):
                    for dy in range(3):
                        largest[i][j] = max(largest[i][j], grid[i + dx][j + dy])
        return largest


if __name__ == '__main__':
    solution = Solution().largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
    ic(solution)
