#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-12 23:05
FileName: P0223. 矩形面积
Description:
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        area3 = max(0, cx2 - cx1) * max(0, cy2 - cy1)
        return area1 + area2 - area3


if __name__ == '__main__':
    solution = Solution().computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2)
    print(solution)
