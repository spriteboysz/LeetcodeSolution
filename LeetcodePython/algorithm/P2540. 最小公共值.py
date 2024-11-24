#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:29
FileName: P2540. 最小公共值
Description:
"""
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = list(set(nums1) & set(nums2))
        return -1 if not seen else min(seen)


if __name__ == '__main__':
    solution = Solution().getCommon(nums1=[1, 2, 3], nums2=[2, 4])
    print(solution)
