#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:25
FileName: P2540. 最小公共值.py
Description:
"""
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(list(set(nums1) & set(nums2)), default=-1)


if __name__ == '__main__':
    solution = Solution().getCommon(nums1=[1, 2, 3], nums2=[2, 4])
    print(solution)
