#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-26 20:43
FileName: P3899. 三角形的内角度数.py
Description:
"""
from math import degrees, acos


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        a, b, c = sides
        if a + b <= c:
            return []

        angle1 = degrees(acos((b * b + c * c - a * a) / (b * c * 2)))
        angle2 = degrees(acos((a * a + c * c - b * b) / (a * c * 2)))
        return [angle1, angle2, 180 - angle1 - angle2]


if __name__ == '__main__':
    solution = Solution().internalAngles(sides=[3, 4, 5])
    print(solution)
