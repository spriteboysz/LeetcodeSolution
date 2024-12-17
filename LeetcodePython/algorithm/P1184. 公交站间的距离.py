#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-16 22:56
FileName: P1184. 公交站间的距离
Description:
"""
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, end = min(start, destination), max(start, destination)
        curr = sum(distance[start:end])
        return min(sum(distance) - curr, curr)


if __name__ == '__main__':
    solution = Solution().distanceBetweenBusStops(distance=[7,10,1,12,11,14,5,0], start=7, destination=2)
    print(solution)
