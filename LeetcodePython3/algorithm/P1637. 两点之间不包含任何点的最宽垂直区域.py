#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:11
FileName: P1637. 两点之间不包含任何点的最宽垂直区域.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        nums = sorted(x for x, _ in points)
        return max(num2 - num1 for num1, num2 in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]])
    print(solution)
