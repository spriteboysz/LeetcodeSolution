#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 12:13
FileName: P3128. 直角三角形
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows, columns = defaultdict(int), defaultdict(int)
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    rows[i] += 1
                    columns[j] += 1
        cnt = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    cnt += (rows[i] - 1) * (columns[j] - 1)
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfRightTriangles(grid=[[0, 1, 0], [0, 1, 1], [0, 1, 0]])
    ic(solution)
