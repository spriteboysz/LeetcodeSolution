#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 17:45
FileName: LCR 035. 最小时间差
Description:
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) != len(timePoints):
            return 0
        points = [int(hh) * 60 + int(mm) for hh, mm in map(lambda el: el.split(":"), timePoints)]
        points.sort()
        points.append(24 * 60 + points[0])
        return min([points[i] - points[i - 1] for i in range(1, len(points))])


if __name__ == '__main__':
    solution = Solution().findMinDifference(["23:59", "00:00"])
    print(solution)
