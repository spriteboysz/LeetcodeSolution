#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-07 17:45
FileName: algorithm/P0447. 回旋镖的数量.py
Description: 
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def calc(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        cnt = 0
        for point1 in points:
            dic = defaultdict(int)
            for point2 in points:
                dic[calc(point1, point2)] += 1
            for v in dic.values():
                cnt += v * (v - 1)
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfBoomerangs(points=[[0, 0], [1, 0], [2, 0]])
    ic(solution)
