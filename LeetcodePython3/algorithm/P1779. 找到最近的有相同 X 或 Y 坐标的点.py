#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 13:38
FileName: algorithm/P1779. 找到最近的有相同 X 或 Y 坐标的点.py
Description: 
"""
from math import inf

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distances = []
        for x1, y1 in points:
            if x1 == x or y1 == y:
                distances.append(abs(x1 - x) + abs(y1 - y))
            else:
                distances.append(inf)

        minimum = min(distances)
        for i, distance in enumerate(distances):
            if minimum == distance and minimum != inf:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().nearestValidPoint(
        x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    )
    print('<None>' if solution is None else f'{solution=}')
