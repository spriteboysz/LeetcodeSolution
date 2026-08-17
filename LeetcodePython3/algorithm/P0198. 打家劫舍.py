#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 17:57
FileName: algorithm/P0198. 打家劫舍.py
Description: 
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution().rob([2, 7, 9, 3, 1])
    print(solution)
