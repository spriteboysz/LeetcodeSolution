#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:44
FileName: P1380. 矩阵中的幸运数
Description:
"""
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = [min(row) for row in matrix]
        columns = [max(row) for row in zip(*matrix)]
        return list(set(rows) & set(columns))


if __name__ == '__main__':
    solution = Solution().luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]])
    print(solution)
