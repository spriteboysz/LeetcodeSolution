#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:23
FileName: P1629. 按键持续时间最长的键.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        times = [t2 - t1 for t1, t2 in pairwise([0, *releaseTimes])]
        maximum = max(times)
        return max(key for key, time in zip(keysPressed, times) if time == maximum)


if __name__ == '__main__':
    solution = Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd")
    print(solution)
