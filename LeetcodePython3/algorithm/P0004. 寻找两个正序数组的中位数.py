#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 09:24
FileName: algorithm/P0004. 寻找两个正序数组的中位数.py
Description: 
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        return (nums[n // 2] + nums[n // 2 - 1]) / 2


if __name__ == '__main__':
    solution = Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
    print(solution)
