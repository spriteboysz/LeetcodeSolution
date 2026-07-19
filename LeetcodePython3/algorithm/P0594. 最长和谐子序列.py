#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 09:36
FileName: P0594. 最长和谐子序列.py
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maximum = 0
        for k, v in counter.items():
            if k + 1 in counter:
                maximum = max(maximum, v + counter.get(k + 1, 0))
        return maximum


if __name__ == '__main__':
    solution = Solution().findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7])
    print(solution)
