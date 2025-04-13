#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-13 23:06
FileName: interview/P3516. 找到最近的人.py
Description: 
"""

from icecream import ic


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        m, n = abs(x - z), abs(y - z)
        if m == n:
            return 0
        return 1 if m < n else 2


if __name__ == '__main__':
    solution = Solution().findClosest(x=2, y=7, z=4)
    ic(solution)
