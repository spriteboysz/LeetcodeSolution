#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 22:03
FileName: P1725. 可以形成最大正方形的矩形数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        edges = [min(rectangle) for rectangle in rectangles]
        maximum = max(edges)
        return sum(edge == maximum for edge in edges)


if __name__ == '__main__':
    solution = Solution().countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]])
    ic(solution)
