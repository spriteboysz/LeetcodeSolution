#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 23:24
FileName: P1828. 统计一个圆中点的数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        counts = []
        for a, b, r in queries:
            counts.append(sum((a - x) ** 2 + (b - y) ** 2 <= r ** 2 for x, y in points))
        return counts


if __name__ == '__main__':
    solution = Solution().countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]],
                                      queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]])
    ic(solution)
