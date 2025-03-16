#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:51
FileName: algorithm/P1629. 按键持续时间最长的键.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maximum_time, maximum_char = 0, keysPressed[0]
        times = [0, *releaseTimes]
        times = [times[i] - times[i - 1] for i in range(1, len(times))]
        for time, key in zip(times, keysPressed):
            if time > maximum_time:
                maximum_time = time
                maximum_char = key
            elif time == maximum_time and key > maximum_char:
                maximum_char = key
        return maximum_char


if __name__ == '__main__':
    solution = Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbad")
    ic(solution)
