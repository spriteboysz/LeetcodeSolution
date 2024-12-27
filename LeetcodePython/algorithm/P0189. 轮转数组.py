#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-27 22:07
FileName: P0189. 轮转数组
Description:
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
        print(nums)

if __name__ == '__main__':
    Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)