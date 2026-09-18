#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 13:59
FileName: algorithm/P1227. 飞机座位分配概率.py
Description: 
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


if __name__ == '__main__':
    solution = Solution().nthPersonGetsNthSeat(1)
    print('<None>' if solution is None else f'{solution=}')
