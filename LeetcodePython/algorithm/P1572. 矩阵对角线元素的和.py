#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 22:25
FileName: P1572. 矩阵对角线元素的和
Description:
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i, row in enumerate(mat):
            total += row[i] + row[n - 1 - i]
            if i == n - 1 - i:
                total -= row[i]
        return total


if __name__ == '__main__':
    solution = Solution().diagonalSum(
        mat=[[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]])
    print(solution)
