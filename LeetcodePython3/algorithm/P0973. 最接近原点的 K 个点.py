#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 21:41
FileName: algorithm/P0973. 最接近原点的 K 个点.py
Description: 
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]


if __name__ == '__main__':
    solution = Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2)
    print(solution)
