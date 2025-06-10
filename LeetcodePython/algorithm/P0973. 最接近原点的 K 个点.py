#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-09 23:23
FileName: algorithm/P0973. 最接近原点的 K 个点.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


if __name__ == '__main__':
    solution = Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2)
    ic(solution)
