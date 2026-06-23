#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-22 22:41
FileName: P2956. 找到两个数组中的公共元素.py
Description:
"""
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = set(nums1) & set(nums2)
        return [sum(nums1.count(num) for num in common), sum(nums2.count(num) for num in common)]


if __name__ == '__main__':
    solution = Solution().findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6])
    print(solution)
