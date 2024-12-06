#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:56
FileName: P0324. 摆动排序 II
Description:
"""
from typing import List
from math import ceil


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        nums[::2], nums[1::2] = nums[:ceil(n / 2)][::-1], nums[ceil(n / 2):][::-1]
        print(nums)


if __name__ == '__main__':
    Solution().wiggleSort(nums=[1, 5, 1, 1, 6])
