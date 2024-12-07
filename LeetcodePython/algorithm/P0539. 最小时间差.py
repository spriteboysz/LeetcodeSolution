#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-07 21:59
FileName: P0539. 最小时间差
Description:
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0

        points = []
        for point in timePoints:
            hh, mm = map(int, point.split(':'))
            points.append(hh * 60 + mm)
        diff = set()
        for i, point1 in enumerate(points):
            for point2 in points[:i]:
                diff.add(abs(point1 - point2))
                diff.add(1440 - abs(point1 - point2))
        return min(diff)


if __name__ == '__main__':
    solution = Solution().findMinDifference(timePoints=["00:00", "23:59", "00:00"])
    print(solution)
