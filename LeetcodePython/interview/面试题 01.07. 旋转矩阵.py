#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-01 16:20
FileName: 面试题 01.07. 旋转矩阵
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

        ic(matrix)


if __name__ == '__main__':
    Solution().rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    # ic(solution)
