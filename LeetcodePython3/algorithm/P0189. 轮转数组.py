#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-16 23:43
FileName: P0189. 轮转数组.py
Description:
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


if __name__ == '__main__':
    Solution().rotate(nums=[-1, -100, 3, 99], k=2)
