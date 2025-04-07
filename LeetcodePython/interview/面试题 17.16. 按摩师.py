#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-07 22:57
FileName: interview/面试题 17.16. 按摩师.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i, num in enumerate(nums):
            if i < 2:
                dp.append(num)
            elif i == 2:
                dp.append(nums[0] + nums[2])
            else:
                dp.append(max(dp[i - 2] + num, dp[i - 3] + num))
        return max(dp)


if __name__ == '__main__':
    solution = Solution().massage([2, 1, 4, 5, 3, 1, 1, 3])
    ic(solution)
