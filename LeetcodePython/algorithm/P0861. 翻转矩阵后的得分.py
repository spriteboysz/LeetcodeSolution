#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 17:02
FileName: P0861. 翻转矩阵后的得分
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 1:
                continue
            for i, num in enumerate(row):
                row[i] = 1 - row[i]
        for j in range(1, len(grid[0])):
            cnt = [0, 0]
            for i in range(len(grid)):
                cnt[grid[i][j]] += 1
            if cnt[0] <= cnt[1]:
                continue
            for i in range(len(grid)):
                grid[i][j] = 1 - grid[i][j]
        return sum(int(''.join(map(str, row)), 2) for row in grid)


if __name__ == '__main__':
    solution = Solution().matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    ic(solution)
