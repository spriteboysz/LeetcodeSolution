#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-23 17:52
FileName: P1227. 飞机座位分配概率
Description:
"""

from icecream import ic


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


if __name__ == '__main__':
    solution = Solution().nthPersonGetsNthSeat(1)
    ic(solution)
