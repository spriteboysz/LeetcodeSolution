#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 17:50
FileName: P2293. 极大极小游戏.py
Description:
"""
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 2:
            nums = [[min(nums[i:i + 2]), max(nums[i + 2:i + 4])] for i in range(0, len(nums), 4)]
            nums = sum(nums, [])
        return min(nums)


if __name__ == '__main__':
    solution = Solution().minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2])
    print(solution)
