#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 20:53
FileName: P1266. 访问所有点的最小时间
Description:
"""
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        x1, y1 = points[0]
        for x2, y2 in points[1:]:
            cnt += max(abs(x2 - x1), abs(y2 - y1))
            x1, y1 = x2, y2
        return cnt


if __name__ == '__main__':
    solution = Solution().minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]])
    print(solution)
