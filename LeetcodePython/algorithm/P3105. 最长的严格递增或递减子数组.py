#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-25 23:51
FileName: algorithm/P3105. 最长的严格递增或递减子数组.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maximum, pos1, pos2 = 1, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                maximum = max(maximum, i - pos1 + 1)
            else:
                pos1 = i
            if nums[i] < nums[i - 1]:
                maximum = max(maximum, i - pos2 + 1)
            else:
                pos2 = i
        return maximum


if __name__ == '__main__':
    solution = Solution().longestMonotonicSubarray(nums=[1, 4, 3, 3, 2])
    ic(solution)
