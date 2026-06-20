#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:22
FileName: P1380. 矩阵中的幸运数.py
Description:
"""
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = [min(row) for row in matrix]
        columns = [max(column) for column in zip(*matrix)]
        lucky = []
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == rows[i] == columns[j]:
                    lucky.append(num)
        return lucky


if __name__ == '__main__':
    solution = Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]])
    print(solution)
