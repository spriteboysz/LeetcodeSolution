#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 11:31
FileName: algorithm/P0812. 最大三角形面积.py
Description: 
"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc(point1, point2, point3):
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5

        maximum = 0
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[:i]):
                for k, p3 in enumerate(points[:j]):
                    if len({i, j, k}) != 3:
                        continue
                    maximum = max(maximum, calc(p1, p2, p3))
        return maximum


if __name__ == '__main__':
    solution = Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
    print('<None>' if solution is None else f'{solution=}')
