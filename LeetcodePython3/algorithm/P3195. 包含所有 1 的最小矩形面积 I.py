#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 19:05
FileName: P3195. 包含所有 1 的最小矩形面积 I.py
Description:
"""
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, columns = [], []
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    continue
                rows.append(i)
                columns.append(j)
        return (max(rows) - min(rows) + 1) * (max(columns) - min(columns) + 1)


if __name__ == '__main__':
    solution = Solution().minimumArea(grid=[[0, 1, 0], [1, 0, 1]])
    print(solution)
