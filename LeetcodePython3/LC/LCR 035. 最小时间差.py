#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 08:21
FileName: LCR/LCR 035. 最小时间差.py
Description: 
"""
from itertools import pairwise
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for point in timePoints:
            hh, mm = point.split(':')
            minutes.append(int(hh) * 60 + int(mm))
        if len(minutes) >= 24 * 60:
            return 0
        minutes.sort()
        minutes.append(minutes[0] + 1440)
        return min(t2 - t1 for t1, t2 in pairwise(minutes))


if __name__ == '__main__':
    solution = Solution().findMinDifference(["23:59", "00:00"])
    print(solution)
