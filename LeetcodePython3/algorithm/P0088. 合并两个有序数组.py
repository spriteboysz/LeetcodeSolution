#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 22:17
FileName: P0088. 合并两个有序数组.py
Description:
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[n:] = nums1[:m]
        i, j, k = n, 0, 0
        while i < m + n or j < n:
            if i >= m + n:
                nums1[k] = nums2[j]
                j += 1
            elif j >= n:
                nums1[k] = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    nums1[k] = nums1[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            k += 1
        print(nums1)


if __name__ == '__main__':
    Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
