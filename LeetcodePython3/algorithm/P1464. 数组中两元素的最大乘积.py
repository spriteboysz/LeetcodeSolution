#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 19:29
FileName: P1464. 数组中两元素的最大乘积.py
Description:
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == '__main__':
    solution = Solution().maxProduct(nums=[3, 4, 5, 2])
    print(solution)
