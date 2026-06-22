#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 20:17
FileName: P3000. 对角线最长的矩形的面积.py
Description:
"""
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maximum = max(dimensions, key=lambda el: (el[0] ** 2 + el[1] ** 2, el[0] * el[1]))
        return maximum[0] * maximum[1]


if __name__ == '__main__':
    solution = Solution().areaOfMaxDiagonal(dimensions=[[25, 60], [52, 39], [63, 16], [33, 56]])
    print(solution)
