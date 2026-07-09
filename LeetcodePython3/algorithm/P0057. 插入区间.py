#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-08 22:36
FileName: P0057. 插入区间.py
Description:
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ranges = []
        for s, e in intervals:
            if not ranges or ranges[-1][-1] < s:
                ranges.append([s, e])
            else:
                ranges[-1][-1] = max(ranges[-1][-1], e)
        return ranges


if __name__ == '__main__':
    solution = Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
    print(solution)
