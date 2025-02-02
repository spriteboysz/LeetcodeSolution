#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 22:17
FileName: P2210. 统计数组中峰和谷的数量
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        flags = [False, *[nums[i] == nums[i - 1] for i in range(1, len(nums))]]
        nums = [num for num, flag in zip(nums, flags) if not flag]
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                cnt += 1
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countHillValley(nums=[2, 4, 1, 1, 6, 5])
    ic(solution)
