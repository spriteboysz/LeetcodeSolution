#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-09 22:45
FileName: P2078. 两栋颜色不同且距离最远的房子
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max1 = max2 = 0
        for i, color in enumerate(colors):
            if color != colors[-1]:
                max1 = len(colors) - i - 1
                break
        for i in range(len(colors) - 1, -1, -1):
            if colors[i] != colors[0]:
                max2 = i
                break
        return max(max1, max2)


if __name__ == '__main__':
    solution = Solution().maxDistance(colors=[1, 8, 3, 8, 3])
    ic(solution)
