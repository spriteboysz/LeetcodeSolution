#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 22:17
FileName: P0075. 颜色分类
Description:
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)

if __name__ == '__main__':
    Solution().sortColors(nums = [2,0,2,1,1,0])