#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:15
FileName: P1732. 找到最高海拔
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = acc = 0
        for num in gain:
            acc += num
            maximum = max(maximum, acc)
        return maximum


if __name__ == '__main__':
    solution = Solution().largestAltitude(gain=[-5, 1, 5, 0, -7])
    ic(solution)
