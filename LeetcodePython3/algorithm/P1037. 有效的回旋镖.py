#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 16:21
FileName: algorithm/P1037. 有效的回旋镖.py
Description: 
"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0


if __name__ == '__main__':
    solution = Solution().isBoomerang([[1, 1], [2, 2], [7, 7]])
    print('<None>' if solution is None else f'{solution=}')
