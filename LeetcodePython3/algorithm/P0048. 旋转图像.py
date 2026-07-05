#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:23
FileName: P0048. 旋转图像.py
Description:
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i, row in enumerate(matrix):
            for j, num in enumerate(row[:i]):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i, row in enumerate(matrix):
            row.reverse()

        for i, row in enumerate(matrix):
            print(row)


if __name__ == '__main__':
    Solution().rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
