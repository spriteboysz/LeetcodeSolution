#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:11
FileName: algorithm/P0162. 寻找峰值.py
Description: 
"""
from math import inf

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf, *nums, -inf]
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i - 1
        return -1


if __name__ == '__main__':
    solution = Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print('<None>' if not solution else f'{solution=}')
