#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 11:16
FileName: P0883. 三维形体投影面积
Description:
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = sum([int(num != 0) for row in grid for num in row])
        area += sum([max(row) for row in grid])
        area += sum([max(row) for row in zip(*grid)])
        return area


if __name__ == '__main__':
    solution = Solution().projectionArea([[1, 2], [3, 4]])
    print(solution)
