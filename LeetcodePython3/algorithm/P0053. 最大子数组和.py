#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-17 22:47
FileName: algorithm/P0053. 最大子数组和.py
Description: 
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, curr = nums[0], nums[0]
        for num in nums[1:]:
            curr = max(num + curr, num)
            maximum = max(maximum, curr)
        return maximum


if __name__ == '__main__':
    solution = Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(solution)
