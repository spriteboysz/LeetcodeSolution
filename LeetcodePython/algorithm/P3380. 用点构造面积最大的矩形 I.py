#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-16 22:49
FileName: algorithm/P3380. 用点构造面积最大的矩形 I.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        maximum = -1
        points = [tuple(point) for point in points]
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[:i]):
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) not in points or (x2, y1) not in points:
                    continue
                m, n = points.index((x1, y2)), points.index((x2, y1))
                for k, (x3, y3) in enumerate(points):
                    if k in [i, j, m, n]:
                        continue
                    if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
                        break
                else:
                    maximum = max(maximum, abs(x1 - x2) * abs(y1 - y2))
        return maximum


if __name__ == '__main__':
    solution = Solution().maxRectangleArea(points=[[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [3, 2]])
    ic(solution)
