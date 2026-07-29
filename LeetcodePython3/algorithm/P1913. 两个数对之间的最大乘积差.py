#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:08
FileName: P1913. 两个数对之间的最大乘积差.py
Description:
"""
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


if __name__ == '__main__':
    solution = Solution().maxProductDifference(nums=[4, 2, 5, 9, 7, 4, 8])
    print(solution)
