#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-17 22:40
FileName: algorithm/P3386. 按下时间最长的按钮.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        events = [[0, 0], *events]
        result = [(events[i][0], events[i][1] - events[i - 1][1]) for i in range(1, len(events))]
        return max(result, key=lambda event: (event[1], -event[0]))[0]


if __name__ == '__main__':
    solution = Solution().buttonWithLongestTime(events=[[10, 5], [1, 7]])
    ic(solution)
