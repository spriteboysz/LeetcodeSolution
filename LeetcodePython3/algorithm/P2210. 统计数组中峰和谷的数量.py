#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 23:01
FileName: P2210. 统计数组中峰和谷的数量.py
Description:
"""
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] == nums[i]:
                nums[i] = None
        nums = [num for num in nums if num]
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                cnt += 1
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countHillValley(nums=[2, 4, 1, 1, 6, 5])
    print(solution)
