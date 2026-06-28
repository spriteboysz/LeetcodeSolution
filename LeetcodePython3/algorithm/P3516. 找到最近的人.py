#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 20:05
FileName: P3516. 找到最近的人.py
Description:
"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        t1, t2 = abs(x - z), abs(y - z)
        if t1 == t2:
            return 0
        return 1 if t1 < t2 else 2


if __name__ == '__main__':
    solution = Solution().findClosest(x=2, y=7, z=4)
    print(solution)
