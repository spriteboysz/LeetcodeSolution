#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 11:17
FileName: P3386. 按下时间最长的按钮.py
Description:
"""
from itertools import pairwise
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        events = [[0, 0], *events]
        result = [(i2, event2 - event1) for (i1, event1), (i2, event2) in pairwise(events)]
        return max(result, key=lambda event: (event[1], -event[0]))[0]


if __name__ == '__main__':
    solution = Solution().buttonWithLongestTime(events=[[1, 2], [2, 5], [3, 9], [1, 15]])
    print(solution)
