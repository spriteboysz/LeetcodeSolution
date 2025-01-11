#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 21:26
FileName: P1779. 找到最近的有相同 X 或 Y 坐标的点
Description:
"""
from math import inf
from typing import List

from icecream import ic


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        weights = []
        for a, b in points:
            if a == x or b == y:
                weights.append(abs(a - x) + abs(b - y))
            else:
                weights.append(inf)

        minimum = min(weights)
        for i, weight in enumerate(weights):
            if weight == minimum and weight != inf:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().nearestValidPoint(x=3, y=4, points=[[2, 3]])
    ic(solution)
