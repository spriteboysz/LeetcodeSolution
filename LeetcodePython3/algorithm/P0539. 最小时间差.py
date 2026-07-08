#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-07 23:49
FileName: P0539. 最小时间差.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > len(set(timePoints)):
            return 0
        points = []
        for point in set(timePoints):
            hh, mm = map(int, point.split(':'))
            points.append(hh * 60 + mm)
        points = sorted(points)
        points.append(points[0] + 1440)
        return min(p2 - p1 for p1, p2 in pairwise(points))


if __name__ == '__main__':
    solution = Solution().findMinDifference(timePoints=["00:00", "23:59", "00:00"])
    print(solution)
