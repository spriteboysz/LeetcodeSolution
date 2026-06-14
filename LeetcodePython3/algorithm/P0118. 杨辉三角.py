#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 18:22
FileName: P0118. 杨辉三角.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle
        for i in range(numRows - 1):
            row = triangle[-1]
            triangle.append([1, *[a + b for a, b in pairwise(row)], 1])
        return triangle


if __name__ == '__main__':
    solution = Solution().generate(2)
    print(solution)
