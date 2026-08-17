#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 18:11
FileName: algorithm/P0213. 打家劫舍 II.py
Description: 
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(arr: List[int]):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(rob_range(nums[:-1]), rob_range(nums[1:]))


if __name__ == '__main__':
    solution = Solution().rob([1, 2, 3, 1])
    print(solution)
