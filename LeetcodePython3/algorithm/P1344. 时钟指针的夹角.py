#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 16:22
FileName: algorithm/P1344. 时钟指针的夹角.py
Description: 
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_h = hour * 30 + minutes / 2
        angle_m = minutes * 6
        angle = abs(angle_h - angle_m)
        return min(angle, 360 - angle)


if __name__ == '__main__':
    solution = Solution().angleClock(12, 30)
    print('<None>' if solution is None else f'{solution=}')
