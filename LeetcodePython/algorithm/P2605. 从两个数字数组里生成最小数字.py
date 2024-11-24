#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 14:08
FileName: P2605. 从两个数字数组里生成最小数字
Description:
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                return i
        a, b = min(nums1), min(nums2)
        return min(10 * a + b, 10 * b + a)


if __name__ == '__main__':
    solution = Solution().minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7])
    print(solution)
