#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 23:05
FileName: P1877. 数组中最大数对和的最小值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2)])


if __name__ == '__main__':
    solution = Solution().minPairSum([3, 5, 4, 2, 4, 6])
    ic(solution)
