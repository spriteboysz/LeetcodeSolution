#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:51
FileName: P1572. 矩阵对角线元素的和.py
Description:
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                if i == j or i + j + 1 == len(mat[0]):
                    total += num
        return total


if __name__ == '__main__':
    solution = Solution().diagonalSum(
        mat=[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    )
    print(solution)
