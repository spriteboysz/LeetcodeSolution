#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-27 22:48
FileName: P3131. 找出与数组相加的整数 I
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)


if __name__ == '__main__':
    solution = Solution().addedInteger(nums1=[2, 6, 4], nums2=[9, 7, 5])
    ic(solution)
