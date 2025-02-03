#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 22:20
FileName: P3239. 最少翻转次数使二进制矩阵回文 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, columns = [0] * m, [0] * n
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    rows[i] += 1
                    columns[j] += 1
        pass


if __name__ == '__main__':
    solution = Solution().minFlips(grid=[[0, 1], [0, 1], [0, 0]])
    ic(solution)
