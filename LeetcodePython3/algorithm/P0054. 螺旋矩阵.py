#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 14:51
FileName: P0054. 螺旋矩阵.py
Description:
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rotate(grid):
            return [list(row) for row in zip(*grid)][::-1]

        nums = []
        while matrix:
            nums.extend(matrix[0])
            matrix = rotate(matrix[1:])
        return nums


if __name__ == '__main__':
    solution = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(solution)
