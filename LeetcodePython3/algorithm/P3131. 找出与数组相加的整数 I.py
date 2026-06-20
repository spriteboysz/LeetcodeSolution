#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 18:43
FileName: P3131. 找出与数组相加的整数 I.py
Description:
"""
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        diff =  [num2 - num1 for num1, num2 in zip(nums1, nums2)]
        if len(set(diff)) == 1:
            return diff[0]
        raise ValueError('Error')


if __name__ == '__main__':
    solution = Solution().addedInteger(nums1 = [2,6,4], nums2 = [9,7,5])
    print(solution)
