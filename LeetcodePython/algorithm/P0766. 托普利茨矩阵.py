#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:28
FileName: P0766. 托普利茨矩阵
Description:
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 1 or n == 1:
            return True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution().isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
    print(solution)
