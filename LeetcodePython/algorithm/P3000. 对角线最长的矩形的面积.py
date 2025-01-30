#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 22:01
FileName: P3000. 对角线最长的矩形的面积
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        a, b = max(dimensions, key=lambda el: ((el[0] ** 2 + el[1] ** 2), (el[0] * el[1])))
        return a * b


if __name__ == '__main__':
    solution = Solution().areaOfMaxDiagonal([[9, 3], [8, 6]])
    ic(solution)
