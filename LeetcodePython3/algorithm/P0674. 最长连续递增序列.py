#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 21:21
FileName: P0674. 最长连续递增序列.py
Description:
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maximum, curr = 1, 1
        nums.append(nums[-1])
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                maximum = max(maximum, curr)
                curr = 1
        return maximum


if __name__ == '__main__':
    solution = Solution().findLengthOfLCIS(nums=[1, 3, 5])
    print(solution)
