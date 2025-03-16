#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 10:59
FileName: algorithm/P1800. 最大升序子数组和.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum, curr = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                maximum = max(maximum, curr)
                curr = nums[i]
        return max(maximum, curr)


if __name__ == '__main__':
    solution = Solution().maxAscendingSum(nums=[10, 20, 30, 5, 10, 50])
    ic(solution)
