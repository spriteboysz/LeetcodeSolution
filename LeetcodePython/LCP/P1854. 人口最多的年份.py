#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 16:21
FileName: LCP/P1854. 人口最多的年份.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for start, end in logs:
            years[start - 1950] += 1
            years[end - 1950] -= 1
        maximum, maximum_index, acc = 0, 0, 0
        for i, num in enumerate(years):
            if acc + num > maximum:
                maximum_index = i
                maximum = acc + num
            acc += num
        return maximum_index + 1950


if __name__ == '__main__':
    solution = Solution().maximumPopulation(logs=[[1950, 1961], [1960, 1971], [1970, 1981]])
    ic(solution)
