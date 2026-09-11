#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 16:44
FileName: LC/P2078. 两栋颜色不同且距离最远的房子.py
Description: 
"""
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] != colors[-1]:
            return len(colors) - 1

        d1, d2 = 0, 0
        for i, color in enumerate(colors[1:], start=1):
            if color != colors[0]:
                d1 = i
        for i, color in enumerate(colors[::-1][1:], start=1):
            if color != colors[-1]:
                d2 = i
        return max(d1, d2)


if __name__ == '__main__':
    solution = Solution().maxDistance([1, 1, 1, 6, 1, 1, 1])
    print('<None>' if solution is None else f'{solution=}')
