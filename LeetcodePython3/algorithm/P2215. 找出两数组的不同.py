#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:55
FileName: P2215. 找出两数组的不同.py
Description:
"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == '__main__':
    solution = Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6])
    print(solution)
