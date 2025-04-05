#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 18:52
FileName: algorithm/P1232. 缀点成线.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]:
            if (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
                return False
        return True


if __name__ == '__main__':
    solution = Solution().checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    ic(solution)
