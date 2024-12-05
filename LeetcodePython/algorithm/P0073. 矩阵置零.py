#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 22:09
FileName: P0073. 矩阵置零
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
            for j, _ in enumerate(row):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        print(matrix)


if __name__ == '__main__':
    Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
