#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-02 23:03
FileName: P0283. 移动零
Description:
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[pos] = num
                pos += 1
        nums[pos:] = [0] * (len(nums) - pos)

        print(nums)


if __name__ == '__main__':
    Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
