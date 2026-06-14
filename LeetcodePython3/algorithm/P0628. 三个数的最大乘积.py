#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 11:53
FileName: P0628. 三个数的最大乘积.py
Description:
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


if __name__ == '__main__':
    solution = Solution().maximumProduct(nums=[1, 2, 3, 4])
    print(solution)
