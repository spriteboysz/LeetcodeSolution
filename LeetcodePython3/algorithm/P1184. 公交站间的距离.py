#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-27 22:42
FileName: P1184. 公交站间的距离.py
Description:
"""
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = sorted([start, destination])
        a = sum(distance[start:destination])
        return min(a, sum(distance) - a)


if __name__ == '__main__':
    solution = Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1)
    print(solution)
