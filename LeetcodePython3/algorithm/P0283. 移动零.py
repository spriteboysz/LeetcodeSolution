#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:28
FileName: P0283. 移动零.py
Description:
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[k] = num
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
        print(nums)


if __name__ == '__main__':
    Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
