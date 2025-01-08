#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 21:00
FileName: P2293. 极大极小游戏
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) >= 4:
            n = len(nums)
            for i in range(0, n, 4):
                nums.append(min(nums[i:i + 2]))
                nums.append(max(nums[i + 2:i + 4]))
            nums = nums[n:]
        return min(nums)


if __name__ == '__main__':
    solution = Solution().minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2])
    ic(solution)
