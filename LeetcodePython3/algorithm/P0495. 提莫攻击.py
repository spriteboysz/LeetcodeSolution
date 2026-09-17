#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 11:05
FileName: algorithm/P0495. 提莫攻击.py
Description: 
"""
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt = 0
        for i, t in enumerate(timeSeries[:-1]):
            cnt += min(timeSeries[i + 1] - t, duration)
        return cnt + duration


if __name__ == '__main__':
    solution = Solution().findPoisonedDuration(timeSeries=[1, 4], duration=2)
    print('<None>' if solution is None else f'{solution=}')
