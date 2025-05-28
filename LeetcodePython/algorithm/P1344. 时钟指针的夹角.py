#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-25 20:46
FileName: algorithm/P1344. 时钟指针的夹角.py
Description: 
"""

from icecream import ic


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_h = hour * 30 + minutes / 2
        angle_m = minutes * 6
        angle = abs(angle_h - angle_m)
        return angle if angle < 180 else 360 - angle


if __name__ == '__main__':
    solution = Solution().angleClock(12, 30)
    ic(solution)
