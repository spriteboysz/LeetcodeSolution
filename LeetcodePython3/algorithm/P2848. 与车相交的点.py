#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:44
FileName: P2848. 与车相交的点.py
Description:
"""
from functools import reduce
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        return len(reduce(lambda s1, s2: set(s1) | set(s2), (set(range(a, b + 1)) for a, b in nums)))


if __name__ == '__main__':
    solution = Solution().numberOfPoints(nums=[[3, 6], [1, 5], [4, 7]])
    print(solution)
