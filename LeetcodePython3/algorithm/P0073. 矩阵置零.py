#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 00:04
FileName: P0073. 矩阵置零.py
Description:
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = set(), set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    rows.add(i)
                    columns.add(j)
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if i in rows or j in columns:
                    matrix[i][j] = 0

        for row in matrix:
            print(row)


if __name__ == '__main__':
    Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
