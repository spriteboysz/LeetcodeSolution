#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:56
FileName: P3894. 交通信号灯的颜色.py
Description:
"""


class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return 'Green'
        if timer == 30:
            return 'Orange'
        if 30 < timer <= 90:
            return 'Red'
        return 'Invalid'


if __name__ == '__main__':
    solution = Solution().trafficSignal(60)
    print(solution)
