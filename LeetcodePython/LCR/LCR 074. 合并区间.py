#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-14 23:10
FileName: LCR/LCR 074. 合并区间.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda el: (el[0], el[1]))
        ranges = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s > end:
                ranges.append([start, end])
                start = s
            end = max(end, e)
        ranges.append([start, end])
        return ranges




if __name__ == '__main__':
    solution = Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]])
    ic(solution)
