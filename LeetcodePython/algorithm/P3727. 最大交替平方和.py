#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-06 22:13
FileName: P3727. 最大交替平方和.py
Description:
"""
from math import ceil
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        def process(index):
            return 1 if index < ceil(len(nums) / 2) else -1

        return sum(num * num * process(i) for i, num in enumerate(sorted(nums, key=abs, reverse=True)))


if __name__ == '__main__':
    solution = Solution().maxAlternatingSum(nums=[1, -1, 2, -2, 3, -3])
    print(solution)
