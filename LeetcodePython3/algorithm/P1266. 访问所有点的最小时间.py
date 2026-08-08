#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-08 11:51
FileName: P1266. 访问所有点的最小时间.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calc(point1, point2)->int:
            x1, y1 = point1
            x2, y2 = point2
            return max(abs(x1 - x2), abs(y1 - y2))

        return sum(calc(p1, p2) for p1, p2 in pairwise(points))


if __name__ == '__main__':
    solution = Solution().minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]])
    print(solution)
