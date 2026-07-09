#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 23:20
FileName: P1828. 统计一个圆中点的数目.py
Description:
"""
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def check(point, circle):
            x, y = point
            a, b, r = circle
            return (x - a) ** 2 + (y - b) ** 2 <= r * r

        return [sum(check(p, query) for p in points) for query in queries]


if __name__ == '__main__':
    solution = Solution().countPoints(
        points=[[1, 3], [3, 3], [5, 3], [2, 2]],
        queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    )
    print(solution)
