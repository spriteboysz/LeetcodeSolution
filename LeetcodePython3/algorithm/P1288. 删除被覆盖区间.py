#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 08:42
FileName: LC/P1288. 删除被覆盖区间.py
Description: 
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        for i, (a, b) in enumerate(intervals):
            for j, (c, d) in enumerate(intervals):
                if i == j:
                    continue
                if c <= a and b <= d:
                    cnt += 1
                    break
        return len(intervals) - cnt


if __name__ == '__main__':
    solution = Solution().removeCoveredIntervals(intervals=[[14041,32641],[24914,51477],[4983,81235],[62018,77987],[31523,32192],[74196,96194],[16126,52652],[59901,67707],[36502,51366],[56437,86744]])
    print(solution)
