#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-19 20:03
FileName: P3898. 统计每个顶点的度.py
Description:
"""


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in zip(*matrix)]


if __name__ == '__main__':
    solution = Solution().findDegrees(matrix=[[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    print(solution)
