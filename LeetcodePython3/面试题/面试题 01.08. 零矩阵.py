#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 10:46
FileName: 面试题/面试题 01.08. 零矩阵.py
Description: 
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [], []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        for row in matrix:
            print(' '.join(map(str, row)))


if __name__ == '__main__':
    Solution().setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
