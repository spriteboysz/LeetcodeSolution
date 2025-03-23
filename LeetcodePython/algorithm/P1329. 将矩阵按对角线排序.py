#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 10:23
FileName: algorithm/P1329. 将矩阵按对角线排序.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n)]
        for i in range(m):
            for j in range(n):
                diagonals[m - i + j].append(mat[i][j])
        for diagonal in diagonals:
            diagonal.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[m - i + j].pop()
        return mat


if __name__ == '__main__':
    solution = Solution().diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
    ic(solution)
