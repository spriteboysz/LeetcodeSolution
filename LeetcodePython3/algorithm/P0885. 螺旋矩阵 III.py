#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 17:19
FileName: algorithm/P0885. 螺旋矩阵 III.py
Description: 
"""
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    solution = Solution().spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4)
    print(solution)
    for row in solution:
        print('\t'.join(map(str, row)))
