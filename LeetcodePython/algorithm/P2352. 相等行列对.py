#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-21 22:28
FileName: P2352. 相等行列对
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, columns = defaultdict(int), defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for column in zip(*grid):
            columns[tuple(column)] += 1
        return sum(v * columns[row] for row, v in rows.items())


if __name__ == '__main__':
    solution = Solution().equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]])
    ic(solution)
