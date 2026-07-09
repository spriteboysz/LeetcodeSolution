#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:01
FileName: P0807. 保持城市天际线.py
Description:
"""
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(row) for row in grid]
        columns = [max(column) for column in zip(*grid)]
        return sum(min(rows[i], columns[j]) - num for i, row in enumerate(grid) for j, num in enumerate(row))


if __name__ == '__main__':
    solution = Solution().maxIncreaseKeepingSkyline(grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
    print(solution)
