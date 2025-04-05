#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 10:51
FileName: algorithm/P0054. 螺旋矩阵.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = []
        while matrix:
            nums.extend(matrix[0])
            matrix = [list(row) for row in zip(*matrix[1:])][::-1]
        return nums


if __name__ == '__main__':
    solution = Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ic(solution)
