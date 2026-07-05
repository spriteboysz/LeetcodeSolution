#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:37
FileName: P0075. 颜色分类.py
Description:
"""
from typing import List, Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        m, n= counter.get(0, 0), counter.get(1, 0)
        for i in range(len(nums)):
            if i < m:
                nums[i] = 0
            elif m <= i < m + n:
                nums[i] = 1
            else:
                nums[i] = 2

        print(nums)


if __name__ == '__main__':
    Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])
