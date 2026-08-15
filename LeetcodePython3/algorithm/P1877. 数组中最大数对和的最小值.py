#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 20:35
FileName: algorithm/P1877. 数组中最大数对和的最小值.py
Description: 
"""
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-i - 1] for i in range(len(nums) // 2))


if __name__ == '__main__':
    solution = Solution().minPairSum(nums=[3, 5, 2, 3])
    print(solution)
