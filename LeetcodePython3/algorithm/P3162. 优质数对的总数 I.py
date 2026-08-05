#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-04 23:21
FileName: P3162. 优质数对的总数 I.py
Description:
"""
from itertools import product
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        for num1, num2 in product(nums1, nums2):
            if num1 % (num2 * k) == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3)
    print(solution)
