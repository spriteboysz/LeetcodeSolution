#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 13:34
FileName: LC/LCP 55. 采集果实.py
Description: 
"""
import math

from typing import List


class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        cnt = 0
        for type_, count in fruits:
            cnt += time[type_] * math.ceil(count / limit)
        return cnt


if __name__ == '__main__':
    solution = Solution().getMinimumTime([1], [[0, 3], [0, 5]], 2)
    print(solution)
