#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-11 23:24
FileName: P2221. 数组的三角和
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(0, len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]


if __name__ == '__main__':
    solution = Solution().triangularSum(nums=[1, 2, 3, 4, 5])
    ic(solution)
