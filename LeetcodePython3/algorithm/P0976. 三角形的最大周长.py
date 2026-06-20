#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 10:01
FileName: P0976. 三角形的最大周长.py
Description:
"""
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i:i + 3])
        return 0


if __name__ == '__main__':
    solution = Solution().largestPerimeter(nums=[2, 1, 2])
    print(solution)
