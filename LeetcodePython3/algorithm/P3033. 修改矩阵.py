#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 19:03
FileName: P3033. 修改矩阵.py
Description:
"""
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        columns = [max(column) for column in zip(*matrix)]
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == -1:
                    matrix[i][j] = columns[j]
        return matrix


if __name__ == '__main__':
    solution = Solution().modifiedMatrix(matrix = [[1,2,-1],[4,-1,6],[7,8,9]])
    print(solution)
