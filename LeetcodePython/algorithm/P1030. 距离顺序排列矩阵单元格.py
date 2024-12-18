#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 23:30
FileName: P1030. 距离顺序排列矩阵单元格
Description:
"""
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        grid = [[i, j] for i in range(rows) for j in range(cols)]
        return sorted(grid, key=lambda el: abs(el[0] - rCenter) + abs(el[1] - cCenter))


if __name__ == '__main__':
    solution = Solution().allCellsDistOrder(rows=2, cols=3, rCenter=1, cCenter=2)
    print(solution)
