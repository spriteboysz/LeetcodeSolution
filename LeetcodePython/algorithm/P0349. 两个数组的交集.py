#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 23:13
FileName: P0349. 两个数组的交集
Description:
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    solution = Solution().intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
    print(solution)
