#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-27 23:09
FileName: algorithm/P0949. 给定数字能组成的最大时间.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        for seconds in range(24 * 60 - 1, -1, -1):
            hh, mm = divmod(seconds, 60)
            tt = f'{hh:02d}:{mm:02d}'
            if sorted([int(d) for d in tt if d.isdigit()]) == arr:
                return tt
        return ''


if __name__ == '__main__':
    solution = Solution().largestTimeFromDigits(arr=[1, 2, 3, 4])
    ic(solution)
