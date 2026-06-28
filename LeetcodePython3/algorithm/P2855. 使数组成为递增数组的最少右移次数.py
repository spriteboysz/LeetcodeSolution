#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:55
FileName: P2855. 使数组成为递增数组的最少右移次数.py
Description:
"""
from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        index = nums.index(min(nums))
        if nums[index:] + nums[:index] == sorted(nums):
            return (len(nums) - index) % len(nums)
        return -1


if __name__ == '__main__':
    solution = Solution().minimumRightShifts(nums=[1, 2, 3])
    print(solution)
