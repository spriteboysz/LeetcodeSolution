#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 23:06
FileName: P2133. 检查是否每一行每一列都包含全部整数
Description:
"""
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [set(row) for row in matrix]
        columns = [set(column) for column in zip(*matrix)]
        return all([seen == set(range(1, n + 1)) for seen in [*rows, *columns]])


if __name__ == '__main__':
    solution = Solution().checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    print(solution)
