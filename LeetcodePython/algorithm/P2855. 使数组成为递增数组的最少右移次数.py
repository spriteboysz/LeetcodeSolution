#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-16 11:34
FileName: algorithm/P2855. 使数组成为递增数组的最少右移次数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        index = nums.index(min(nums))
        if nums[index:] + nums[:index] == sorted(nums):
            return (len(nums) - index) % len(nums)
        return -1


if __name__ == '__main__':
    solution = Solution().minimumRightShifts(nums=[3, 4, 5, 1, 2])
    ic(solution)
