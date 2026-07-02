#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-30 22:42
FileName: P3898. 统计每个顶点的度.py
Description:
"""


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]


if __name__ == '__main__':
    solution = Solution().findDegrees(matrix=[[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    print(solution)
