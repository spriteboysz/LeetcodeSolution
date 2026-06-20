#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:30
FileName: P2133. 检查是否每一行每一列都包含全部整数.py
Description:
"""
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(set(row)) == len(matrix) for row in matrix) and all(
            len(set(column)) == len(matrix) for column in zip(*matrix))


if __name__ == '__main__':
    solution = Solution().checkValid(matrix=[[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    print(solution)
