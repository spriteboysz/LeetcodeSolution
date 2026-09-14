#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-11 14:25
FileName: LC/P2352. 相等行列对.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for col in zip(*grid):
            cols[tuple(col)] += 1
        return sum(v * cols.get(k, 0) for k, v in rows.items())


if __name__ == '__main__':
    solution = Solution().equalPairs([
        [3, 1, 2, 2],
        [1, 4, 4, 5],
        [2, 4, 2, 2],
        [2, 4, 2, 2]
    ])
    print('<None>' if solution is None else f'{solution=}')
