#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:18
FileName: P0883. 三维形体投影面积.py
Description:
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(num != 0 for num in sum(grid, [])) + sum(max(row) for row in grid) + sum(
            max(list(row)) for row in zip(*grid))


if __name__ == '__main__':
    solution = Solution().projectionArea([[1, 2], [3, 4]])
    print(solution)
