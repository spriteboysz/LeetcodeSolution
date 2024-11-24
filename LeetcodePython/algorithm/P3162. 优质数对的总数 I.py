#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:41
FileName: P3162. 优质数对的总数 I
Description:
"""
from itertools import product
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum([num1 % (num2 * k) == 0 for num1, num2 in product(nums1, nums2)])


if __name__ == '__main__':
    solution = Solution().numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1)
    print(solution)
