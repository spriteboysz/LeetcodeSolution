#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-17 23:11
FileName: algorithm/P1401. 圆和矩形是否有重叠.py
Description: 
"""

from icecream import ic


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def calc(i: int, j: int, k: int) -> int:
            if i <= k <= j:
                return 0
            return i - k if k < i else k - j

        a = calc(x1, x2, xCenter)
        b = calc(y1, y2, yCenter)
        return a * a + b * b <= radius * radius


if __name__ == '__main__':
    solution = Solution().checkOverlap(radius=1, xCenter=0, yCenter=0, x1=1, y1=-1, x2=3, y2=1)
    ic(solution)
