#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 11:40
FileName: algorithm/P1030. 距离顺序排列矩阵单元格.py
Description: 
"""
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        points = [[i, j] for i in range(rows) for j in range(cols)]
        return sorted(points, key=lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))


if __name__ == '__main__':
    solution = Solution().allCellsDistOrder(rows=2, cols=3, rCenter=1, cCenter=2)
    print('<None>' if solution is None else f'{solution=}')
