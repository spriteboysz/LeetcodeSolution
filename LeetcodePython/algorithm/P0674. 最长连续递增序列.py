#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:40
FileName: algorithm/P0674. 最长连续递增序列.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maximum, curr = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                maximum = max(maximum, curr)
                curr = 1
        return max(maximum, curr)


if __name__ == '__main__':
    solution = Solution().findLengthOfLCIS(nums=[1, 3, 5, 7])
    ic(solution)
