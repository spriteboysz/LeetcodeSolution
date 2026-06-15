#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:29
FileName: P1619. 删除某些元素后的数组均值.py
Description:
"""
from statistics import mean
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        m = int(len(arr) * 0.05)
        return mean(sorted(arr)[m:-m])


if __name__ == '__main__':
    solution = Solution().trimMean(arr=[6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0])
    print(solution)
