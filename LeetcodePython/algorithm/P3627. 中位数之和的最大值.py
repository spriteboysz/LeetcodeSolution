#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-01-18 17:47
FileName: P3627. 中位数之和的最大值.py
Description:
"""
from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[len(nums) // 3::2])


if __name__ == '__main__':
    s = Solution().maximumMedianSum(nums=[2, 1, 3, 2, 1, 3])
    print(s)
