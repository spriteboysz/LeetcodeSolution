#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 10:36
FileName: P0812. 最大三角形面积
Description:
"""
from itertools import combinations
from typing import List

from icecream import ic


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc(point1, point2, point3):
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5

        return max(calc(a, b, c) for a, b, c in combinations(points, 3))


if __name__ == '__main__':
    solution = Solution().largestTriangleArea(points=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
    ic(solution)
