#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-08 23:08
FileName: interview/面试题 10.11. 峰与谷.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        m = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:m], nums[m:]
        ic(nums)


if __name__ == '__main__':
    Solution().wiggleSort([5, 3, 1, 2, 3])
    Solution().wiggleSort([5, 3, 1, 2])
