#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 22:58
FileName: interview/面试题 16.10. 生存人数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        years = [0] * 102
        for s, e in zip(birth, death):
            years[s - 1900] += 1
            years[e - 1900 + 1] -= 1
        maximum, maximum_index, acc = 0, 0, 0
        for i, num in enumerate(years):
            acc += num
            if acc > maximum:
                maximum = acc
                maximum_index = i + 1900
        return maximum_index

if __name__ == '__main__':
    solution = Solution().maxAliveYear(birth=[1900, 1901, 1950], death=[1948, 1951, 2000])
    ic(solution)
