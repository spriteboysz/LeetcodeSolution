#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 00:42
FileName: LCR/LCR 074. 合并区间.py
Description: 
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda el: el[0])
        merged = [intervals[0]]
        for left, right in intervals[1:]:
            if left <= merged[-1][-1]:
                merged[-1][-1] = max(merged[-1][-1], right)
            else:
                merged.append([left, right])
        return merged


if __name__ == '__main__':
    solution = Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
    print(solution)
