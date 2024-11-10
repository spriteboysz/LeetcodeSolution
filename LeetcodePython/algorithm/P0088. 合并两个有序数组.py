#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 18:21
FileName: P0088. 合并两个有序数组
Description:
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2
        nums1.sort()
        print(nums1)


if __name__ == '__main__':
    Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
