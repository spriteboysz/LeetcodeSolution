#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 21:36
FileName: P3769. 二进制反射排序.py
Description:
"""
from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda el: (int(bin(el)[2:][::-1]), el))


if __name__ == '__main__':
    s = Solution().sortByReflection([4, 5, 4])
    print(s)
