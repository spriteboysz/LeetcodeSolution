#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 22:50
FileName: interview/面试题 16.17. 连续数列.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    solution = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    ic(solution)
