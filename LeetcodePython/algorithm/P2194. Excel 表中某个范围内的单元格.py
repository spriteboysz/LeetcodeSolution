#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 22:22
FileName: P2194. Excel 表中某个范围内的单元格
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        row1, col1, _, row2, col2 = s
        cells = []
        for row in range(ord(row1), ord(row2) + 1):
            for col in range(int(col1), int(col2) + 1):
                cells.append(f'{chr(row)}{col}')
        return cells


if __name__ == '__main__':
    solution = Solution().cellsInRange("K1:L2")
    ic(solution)
