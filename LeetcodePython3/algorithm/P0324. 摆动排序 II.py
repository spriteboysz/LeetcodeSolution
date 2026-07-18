#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:01
FileName: P0324. 摆动排序 II.py
Description:
"""
import math
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        >>> [1, 5, 1, 1, 6, 4]
        [1, 6, 1, 5, 1, 4]
        Do not return anything, modify nums in-place instead.
        """
        sored_nums = sorted(nums)
        m = math.ceil(len(nums) / 2)
        nums[::2], nums[1::2] = sored_nums[:m][::-1], sored_nums[m:][::-1]
        print(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
