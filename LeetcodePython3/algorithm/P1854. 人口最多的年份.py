#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 17:26
FileName: P1854. 人口最多的年份.py
Description:
"""
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for start, end in logs:
            years[start - 1950] += 1
            years[end - 1950] -= 1
        curr = 0
        for i, year in enumerate(years):
            curr += year
            years[i] = curr
        maximum = max(years)
        for i, year in enumerate(years):
            if year == maximum:
                return i + 1950
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().maximumPopulation(logs=[[1950, 1961], [1960, 1971], [1970, 1981]])
    print(solution)
