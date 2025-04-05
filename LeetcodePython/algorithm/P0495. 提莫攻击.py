#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 21:45
FileName: algorithm/P0495. 提莫攻击.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt = 0
        for i in range(1, len(timeSeries)):
            if (d := timeSeries[i] - timeSeries[i - 1]) < duration:
                cnt += d
            else:
                cnt += duration
        return cnt + duration


if __name__ == '__main__':
    solution = Solution().findPoisonedDuration(timeSeries=[1, 4], duration=2)
    ic(solution)
