#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 13:29
FileName: P2605. 从两个数字数组里生成最小数字.py
Description:
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for digit in range(10):
            if digit in nums1 and digit in nums2:
                return digit

        min1, min2 = min(nums1), min(nums2)
        return min(10 * min1 + min2, 10 * min2 + min1)


if __name__ == '__main__':
    solution = Solution().minNumber(nums1=[4, 1, 3], nums2=[5, 7])
    print(solution)
