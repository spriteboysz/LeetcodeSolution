#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-25 23:29
FileName: P1725. 可以形成最大正方形的矩形数目.py
Description:
"""
from typing import List, Counter


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        slides = [min(rectangle) for rectangle in rectangles]
        return Counter(slides).get(max(slides), 0)


if __name__ == '__main__':
    solution = Solution().countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]])
    print(solution)
